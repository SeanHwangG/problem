```py
import re
Test_String = input()
pattern = r"(?<=[13579])\d"
match = re.findall(pattern, Test_String)

print("Number of matches :", len(match))
```
