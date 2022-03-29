from __future__ import print_function

import pathlib
import os
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class Problem:
  def __init__(self, pid, group):
    self.pid = pid
    self.group = group

  def __repr__(self):
    return f"[problem: {self.pid}, group: {self.group}]"

  def current_path(self):

    current_path = list(pathlib.Path(".").glob(f"**/{self.pid}.md"))
    if len(current_path) == 0:
      print(self)
      return None

    return current_path[0]

  def correct_path(self):
    return pathlib.Path(self.group) / f"{self.pid}.md"


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
  result = sheet.values().get(spreadsheetId="1Wo5Z4E3ViISDVqQ5ATPbtEglzuaVEbCFIzMJ0GpiRiQ", range='D2:E9000').execute()
  values = result.get('values', [])

  return [Problem(row[0], row[1]) for row in values if len(row) == 2]


def move_problems(problem):
  for problem in problems:
    if problem.current_path():
      pathlib.Path(problem.correct_path().parent).mkdir(exist_ok=True)
      problem.current_path().rename(problem.correct_path())


if __name__ == '__main__':
  problems = extract_problems()
  move_problems(problems)
