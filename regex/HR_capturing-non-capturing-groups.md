```py
import re
pattern = r'(ok){3,}'
print(str(bool(re.search(pattern, input()))).lower())
```
