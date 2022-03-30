from __future__ import print_function

import pathlib
import os
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class Group:
  def __init__(self, gid):
    self.gid = gid

class Problem:
  def __init__(self, pid, gid, sample="", english=""):
    self.pid = pid
    self.gid = gid
    self.sample = sample
    self.english = english
    self.cur_path = None

  def __repr__(self):
    return f"[problem: {self.pid}, gid: {self.gid}]"

  """
  @property
  def cur_path(self):
    if self.cur_path:
      return self.cur_path

    current_path = list(pathlib.Path(".").glob(f"**/{self.pid}.md"))
    if len(current_path) == 0:
      print(self)
      return None

    return current_path[0]
  """

  def correct_path(self):
    return pathlib.Path(self.gid) / f"{self.pid}.md"


def extract_problems():
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first time.
  if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json',
                                                  ['https://www.googleapis.com/auth/spreadsheets.readonly'])

  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file("credentials.json",
                                                       ['https://www.googleapis.com/auth/spreadsheets.readonly'])
      creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
      token.write(creds.to_json())

  service = build('sheets', 'v4', credentials=creds)

  sheet = service.spreadsheets()
  result = sheet.values().get(spreadsheetId="1Wo5Z4E3ViISDVqQ5ATPbtEglzuaVEbCFIzMJ0GpiRiQ", range='Problem!D2:G9000').execute()
  values = result.get('values', [])

  return [Problem(row[0], row[1], row[2], row[3]) for row in values if len(row) == 4]


def move_problems(problems):
  for problem in problems:
    if problem.cur_path:
      pathlib.Path(problem.cur_path.parent).mkdir(exist_ok=True)
      problem.cur_path.rename(problem.correct_path())

def update_meta_problems(problems: Problem):
  for p in problems:
    solution = p.correct_path().read_text().split("## Solution\n")[-1]
    p.correct_path().write_text(f"""# {p.pid}\n\n{p.english}\n\n```txt\n{p.sample}\n```\n\n## Solution\n{solution}""")

if __name__ == '__main__':
  problems = extract_problems()
  # move_problems(problems)
  update_meta_problems(problems)
