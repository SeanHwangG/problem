# [LC_smallest-good-base](https://leetcode.com/problems/smallest-good-base)

Given an integer n represented as a string, return the smallest good base of n
We call k >= 2 a good base of n, if all digits of n base k are 1's


```txt
Input: n = "13"
Output: "3"
```

## Solution

* py

```py
def smallestGoodBase(self, n: str) -> str:
  def is_valid(base, size):
    """returns 0 if total == n, pos if n > total and neg if n < total"""
    total = sum(base ** i for i in range(size))
    return n - total
  n = int(n)
  N = len(bin(n)[2:])
  for size in range(N, 0, -1):
    lo, hi = 2, n - 1
    while lo <= hi:
      mi = (lo + hi) // 2
      v = is_valid(mi, size)
      if v < 0:
        hi = mi - 1
      elif v > 0:
        lo = mi + 1
      else:
        return str(mi)
```
