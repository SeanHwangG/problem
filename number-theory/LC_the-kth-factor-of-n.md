```py
import math
def kthFactor(self, n: int, k: int) -> int:
  factors = []
  for i in range(1, math.isqrt(n) + 1):
    if n % i == 0:
      factors.append(i)
      k -= 1
    if k == 0: return i
  if factors[-1] ** 2 == n: factors.pop()
  if k > len(factors): return -1
  return n // factors[-k]
```
