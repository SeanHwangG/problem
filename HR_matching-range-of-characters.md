```py
import re
pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'
print(str(bool(re.search(pattern, input()))).lower())
```
