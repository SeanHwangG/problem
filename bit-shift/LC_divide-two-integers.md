# [LC_divide-two-integers](https://leetcode.com/problems/divide-two-integers)

Implement division without using multiplication, division, and mod

```txt
Input: dividend = 7, divisor = -3
Output: -2
```

## Solution

```py
def divide(self, A, B):
  if A == -2147483648 and B == -1: return 2147483647
  a, b, res = abs(A), abs(B), 0
  for x in range(32)[::-1]:
    if (a >> x) >= b:
      res += 1 << x
      a -= b << x
  return res if (A > 0) == (B > 0) else -res
```
