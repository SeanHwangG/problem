```py
import re
class Solution:
  def numUniqueEmails(self, emails: List[str]) -> int:
    set_ = set()
    for e in emails:
      local, domain = e.split('@')
      local = re.sub('[.]+','',local)
      local = re.sub('[+][a-zA-Z0-9\W]+','',local)
      set_.add(f"{local}@{domain}")
    return len(set_)
```
