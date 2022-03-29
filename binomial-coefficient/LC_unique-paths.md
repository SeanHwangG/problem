```py
from math import comb
def uniquePaths(self, m: int, n: int) -> int:
  return comb(m + n - 2, m - 1)
```
