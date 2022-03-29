```py
import re
for i in range(int(input())):
  print("YES" if re.match(r'[A-Z]{5}[0-9]{4}[A-Z]{1}', input()) else "NO")
```
