```py
import re, sys
for s in filter(re.match(r"(?i:hi\s[^d])", sys.stdin)):
  print(s.strip())
```