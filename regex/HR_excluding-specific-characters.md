```py
import re

pattern = r'^[^\d][^aeiou][^bcDF]\S[^AEIOU][^.,]$'
print(str(bool(re.search(pattern, input()))).lower())
```
