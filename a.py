import os
import json
from pathlib import Path

p = Path(".")
with open("a.json", "r") as f:
  dic = json.load(f)

for l in p.glob("LC_*"):
  name = (str(l)[3:-3])
  print(dic[name])
  os.rename(l, "LC_" + dic[name] + ".md")
