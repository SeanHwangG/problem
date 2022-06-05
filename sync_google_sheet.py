from __future__ import print_function
from __future__ import annotations

from itertools import islice
from pathlib import Path
import re
import os
import os.path
import itertools

from dataclasses import dataclass, field

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

PROBLEM_DIR = Path("/Users/sean/blog/repo/problem/")

EXTRACT_RE = r"# \[.*\]\((?P<url>.*)\)"


@dataclass
class Problem:
  pid: str
  path: Path
  url: str

  # english: str
  # sample: str
  # group: Group

  def __repr__(self):
    return f"[problem: {self.pid}, path: {self.path}]"

  # def to_list(self):
  #   return [self.path, self.group, self.url, self.sample, self.english]

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
      contest, problem = re.findall(r"CF_([0-9]+)([A-Z0-9]*)", self.pid)[0]
      return f"[{self.pid}](https://codeforces.com/contest/{contest}/{problem})"

  def correct_path(self):
    return PROBLEM_DIR / self.path.lower() / self.gid / f"{self.pid}.md"


@dataclass
class Group:
  gid: str
  path: Path

  @staticmethod
  def valid(path: Path):
    ignore_dirs = ["venv", ".git", ".mypy_cache", "images"]
    return path.is_dir() and path.name not in ignore_dirs

  def extract_problems(self) -> list[Problem]:
    problems = []
    for p in self.path.glob("*/*.md"):
      if m := re.search(EXTRACT_RE, p.read_text()):
        problems.append(Problem(
            p.name,
            p,
            m.group("url"),
        ))
      else:
        print("Incorrect format matched", p)
    return problems


@dataclass
class Repo:
  path: Path

  def extract_group(self) -> list[Group]:
    return [
        Group(child.name, child)
        for child in self.path.iterdir()
        if Group.valid(child)
    ]


@dataclass
class Excel:
  sheet_id: str
  pid2problem: dict[str, Problem] = field(default_factory=lambda: {})

  def write(self):
    pass

  def update_cred(self):
    cred = None
    if os.path.exists("token.json"):
      cred = Credentials.from_authorized_user_file(
          "token.json",
          ["https://www.googleapis.com/auth/spreadsheets.readonly"])

    if not cred or not cred.valid:
      if cred and cred.expired and cred.refresh_token:
        cred.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            PROBLEM_DIR / "credentials.json",
            ["https://www.googleapis.com/auth/spreadsheets.readonly"],
        )
        cred = flow.run_local_server(port=0)
      with open("token.json", "w") as token:
        token.write(cred.to_json())

    self.service = build("sheets", "v4", credentials=cred)

  def read_problem_ids(self) -> list[str]:
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.

    sheet = self.service.spreadsheets()
    result = (sheet.values().get(
        spreadsheetId=self.sheet_id,
        range="Problem!F2:F9000",
    ).execute())
    return [pid[0] for pid in result.get("values", [])]

  def write_problem_ids(self):
    pass


if __name__ == "__main__":
  # excel = Excel("1Wo5Z4E3ViISDVqQ5ATPbtEglzuaVEbCFIzMJ0GpiRiQ")
  repo = Repo(Path("/Users/sean/blog/repo/problem"))
  groups = repo.extract_group()
  problems = list(
      itertools.chain.from_iterable(
          group.extract_problems() for group in groups))
  for problem in problems:
    print(problem)
    lines = problem.path.read_text().split("\n")
    diff = True
    result = ""
    tp_re = r"  ```(.*)"
    for i, line in enumerate(lines):
      if line.startswith("##"):
        diff = False
      if diff and re.match(tp_re, line[i + 1]):
        m = re.match(tp_re, line[i + 1])
        new_line = f"* {m.group(1)}\n"
      else:
        new_line = line
      result += new_line.rstrip() + "\n"
      break

    problem.path.write_text(result[:-1])
  # excel.update_cred()
  # excel.write(problems)
  # problem_ids = excel.read_problem_ids()
  # problems = excel.extract_problems()
  # problems = write_problems()
