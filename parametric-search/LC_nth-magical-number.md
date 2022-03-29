```py
import math
def nthMagicalNumber(self, N, A, B):
  l, r, lcm = 2, 10 ** 14, math.lcm(A, B)
  while l < r:
    m = (l + r) // 2
    if m // A + m // B - m // lcm < N: # inclusion exclusion formula
      l = m + 1
    else:
      r = m
  return l % (10**9 + 7)
```
