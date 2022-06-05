# [LC_nth-magical-number](https://leetcode.com/problems/nth-magical-number)

```en
Positive integer is magical if it is divisible by either a or b
Given the three integers n, a, and b, return the nth magical number modulo 10 ** 9 + 7
```

```txt
Input: n = 1, a = 2, b = 3
Output: 2
```

## Solution

* py

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
