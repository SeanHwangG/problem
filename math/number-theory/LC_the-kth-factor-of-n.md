# [LC_the-kth-factor-of-n](https://leetcode.com/problems/the-kth-factor-of-n)

Consider a list of all factors of n sorted in ascending order
return kth factor in this list or return -1 if n has less than k factors

```txt
Input: n = 12, k = 3
Output: 3
```

## Solution

* py

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
