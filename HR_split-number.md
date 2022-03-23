```py
import re
for i in range(int(input())):
  a, b, c = (re.sub(r"[ -]", " ", input())).split()
  print(f"CountryCode={a},LocalAreaCode={b},Number={c}")
```
