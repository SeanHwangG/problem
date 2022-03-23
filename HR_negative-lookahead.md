```py
import re

Test_String = input()
pattern = r"(.)(?!\1)"
match = re.findall(pattern, Test_String)

print("Number of matches :", len(match))
```
