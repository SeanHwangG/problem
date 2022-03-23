```py
import re
pattern = r"^((\d{8})|(\d{2}-\d{2}-\d{2}-\d{2}))$"
print(str(bool(re.search(pattern, input()))).lower())
```
