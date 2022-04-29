from __future__ import print_function

from pathlib import Path
import re
import os
import os.path

from dataclasses import dataclass

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


@dataclass
class Problem:
    path: str
    gid: str
    pid: str
    sample: str
    english: str
    cur_path = ""

    def __repr__(self):
        return f"[problem: {self.pid}, gid: {self.gid}, cur_path: {self.cur_path}]"

    def link(self):
        category = self.pid[:2]
        value = self.pid[3:]
        if category == "BJ":
            return f"[{self.pid}](https://acmicpc.net/problem/{value})"
        if category == "KT":
            return f"[{self.pid}](https://open.kattis.com/problems/{value})"
        if category == "HR":
            return f"[{self.pid}](https://www.hackerrank.com/challenges/{value})"
        if category == "LC":
            return f"[{self.pid}](https://leetcode.com/problems/{value})"
        if category == "CF":
            contest, problem = re.findall(r"CF_([0-9]+)([A-Z0-9]*)",
                                          self.pid)[0]
            return f"[{self.pid}](https://codeforces.com/contest/{contest}/{problem})"

    def correct_path(self):
        return Path(self.path.lower()) / self.gid / f"{self.pid}.md"


def update_cur_paths(problems: list[Problem]):
    pid2problem = {p.pid: p for p in problems}
    for p in Path(".").glob("**/*.md"):
        if p.stem in pid2problem:
            pid2problem[p.stem].cur_path = p
        else:
            print(p.stem, "missing")
    return problems


def extract_problems():
    print("Extracting Problem")
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file(
            'token.json',
            ['https://www.googleapis.com/auth/spreadsheets.readonly'])

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                ['https://www.googleapis.com/auth/spreadsheets.readonly'])
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId="1Wo5Z4E3ViISDVqQ5ATPbtEglzuaVEbCFIzMJ0GpiRiQ",
        range='Problem!D2:H9000').execute()
    values = result.get('values', [])

    problems = [
        Problem(row[0], row[1], row[2], row[3],
                row[4] if len(row) == 5 else "") for row in values
        if len(row) >= 4
    ]
    print(f"Extracted {len(problems)} Problem")
    return problems


def move_problems(problems):
    print("Moving Problem")
    for problem in problems:
        if Path(problem.cur_path) != problem.correct_path():
            problem.correct_path().parent.mkdir(exist_ok=True)
            Path(problem.cur_path).rename(problem.correct_path())


def update_meta_problems(problems: Problem):
    print("Updating meta problem")
    for p in problems:
        solution = p.correct_path().read_text().split("## Solution\n\n")[-1]
        p.correct_path().write_text(
            f"""# {p.link()}\n\n{p.english}\n\n```txt\n{p.sample}\n```\n\n## Solution\n\n{solution}"""
        )


def remove_empty_dir(path):
    [
        os.removedirs(p) for p in Path(path).glob('**/*')
        if p.is_dir() and len(list(p.iterdir())) == 0
    ]


if __name__ == '__main__':
    problems = extract_problems()
    problems = update_cur_paths(problems)
    move_problems(problems)
    update_meta_problems(problems)
    remove_empty_dir(".")
