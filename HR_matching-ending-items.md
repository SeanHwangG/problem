```py
import re
pattern = r'^[a-zA-Z]*s$'
print(str(bool(re.search(pattern, input()))).lower())
```
