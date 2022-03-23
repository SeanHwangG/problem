```py
import re
pattern = r'^\d+[A-Z]+[a-z]+$'
print(str(bool(re.search(pattern, input()))).lower())
```
