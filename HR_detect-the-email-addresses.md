```py
import re
N = int(input())
myStr = " ".join([input() for i in range(N)])
print(";".join(sorted(set([i for i in re.findall(r"([\w.]+@[\w.]+\w+)", myStr)]))))
```
