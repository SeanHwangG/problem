```py
import re

pattern = r'^\d\w\w\w\w\.$'
print(str(bool(re.search(pattern, input()))).lower())
```
