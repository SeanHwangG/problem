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

PROBLEM_DIR = Path(Path.home() / "blog/repo/problem/")

EXTRACT_RE = r"# \[.*\]\((?P<url>.*)\)"


@dataclass
class Problem:
  """
  """
  pid: str
  path: Path
  group: str
  sid: str
  url: str

  tc: str = ""
  en: str = ""
  kr: str = ""

  def to_list(self):
    """
    """
    return [
        f'=hyperlink("https://github.com/SeanHwangG/problem/blob/main/{self.sid}/{self.group}/{self.pid}.md", "sol")',
        self.sid, self.group, f'=hyperlink("{self.url}", "{self.pid}")',
        self.tc, self.en, self.kr
    ]

  def extract_problem(self) -> dict[str, str]:
    ret: dict[str, str] = {}
    key = val = ""

    for line in self.path.read_text().split("\n"):
      if line.startswith("  ```") and len(line) > 5:
        key = line[5:]
        val = ""
      elif line == "  ```":
        if hasattr(self, key):
          self.__setattr__(key, val[:-1])
      elif key:
        val += line[2:] + "\n"
    return ret


@dataclass
class Subject:
  sid: str
  path: Path

  @staticmethod
  def valid(path: Path):
    ignore_dirs = ["venv", ".git", ".mypy_cache", "images"]
    return path.is_dir() and path.name not in ignore_dirs

  def extract_problems(self) -> list[Problem]:
    extracted_problems = []
    for p in self.path.glob("*/*_*.md"):
      if m := re.search(EXTRACT_RE, p.read_text()):
        p = Problem(
            p.stem,
            p,
            p.parent.name,
            self.sid,
            m.group("url"),
        )
        p.extract_problem()
        extracted_problems.append(p)
      else:
        print("Incorrect format matched", p)
    return extracted_problems


@dataclass
class Repo:
  path: Path

  def extract_subject(self) -> list[Subject]:
    return [
        Subject(child.name, child)
        for child in self.path.iterdir()
        if Subject.valid(child)
    ]


@dataclass
class Excel:
  sheet_id: str
  sheet: Any = None

  def write(self):
    pass

  def update_cred(self):
    cred = None
    if os.path.exists("token.json"):
      print("token exists")
      cred = Credentials.from_authorized_user_file(
          "token.json", ["https://www.googleapis.com/auth/spreadsheets"])

    if not cred or not cred.valid:
      if cred and cred.expired and cred.refresh_token:
        print("Refreshing token")
        cred.refresh(Request())
      else:
        print("New")
        flow = InstalledAppFlow.from_client_secrets_file(
            PROBLEM_DIR / "credentials.json",
            ["https://www.googleapis.com/auth/spreadsheets"],
        )
        cred = flow.run_local_server(port=0)
      with open("token.json", "w") as token:
        token.write(cred.to_json())

    self.sheet = build("sheets", "v4", credentials=cred).spreadsheets()

  def read_problem_ids(self) -> list[str]:
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.

    result = (self.sheet.values().get(
        spreadsheetId=self.sheet_id,
        range="Problem!F2:F9000",
    ).execute())
    return [pid[0] for pid in result.get("values", [])]

  def write_problems(self, problems: list[Problem]):
    body = {
        'valueInputOption':
            "USER_ENTERED",
        "data": [{
            'range': f"Problem!A2:G{len(problems) + 1}",
            'values': [problem.to_list() for problem in problems]
        }]
    }
    result = self.sheet.values().batchUpdate(spreadsheetId=self.sheet_id,
                                             body=body).execute()
    print(result.get('totalUpdatedCells'))


if __name__ == "__main__":
  repo = Repo(Path(Path.home() / "blog/repo/problem"))
  subjects = repo.extract_subject()
  problems = list(
      itertools.chain.from_iterable(
          subject.extract_problems() for subject in subjects))

  excel = Excel("1Wo5Z4E3ViISDVqQ5ATPbtEglzuaVEbCFIzMJ0GpiRiQ")
  excel.update_cred()
  problems = excel.write_problems(problems)
