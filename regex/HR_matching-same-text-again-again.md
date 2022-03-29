```py
import re

pattern = r'^([a-z]\w\s\W\d\D[A-Z][a-z,A-Z][aieouAEIOU]\S)\1$'
print(str(bool(re.search(pattern, input()))).lower())
```
