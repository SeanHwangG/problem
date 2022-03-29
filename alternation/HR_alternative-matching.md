```py
import re
pattern = r'^(Mr|Mrs|Ms|Dr|Er)\.[A-Za-z]+$'  # Do not delete 'r'.

print(str(bool(re.search(pattern, input()))).lower())
```
