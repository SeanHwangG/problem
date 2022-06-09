# [LC_unique-email-addresses](https://leetcode.com/problems/unique-email-addresses)

* en

  ```en
  Every valid email consists of a local local and a domain name, separated by the '@' sign
  Besides lowercase letters, the email may contain one or more '.' or '+'
  '.' is ignored
  '+' is ignored with characters after '+'
  ```

* tc

  ```tc
  Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
  Output: 2
  ```

## Solution

* py

  ```py
  import re

  def numUniqueEmails(self, emails: List[str]) -> int:
    set_ = set()
    for e in emails:
      local, domain = e.split('@')
      local = re.sub('[.]+', '', local)
      local = re.sub('[+][a-zA-Z0-9\W]+','',local)
      set_.add(f"{local}@{domain}")
    return len(set_)
  ```
