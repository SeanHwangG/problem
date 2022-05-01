# [LC_ugly-number](https://leetcode.com/problems/ugly-number)

Given int n, return true if n is an ugly number
Ugly number is a positive number whose prime factors only include 2, 3, and/or 5

```txt
Input: 6
Output: true
```

## Solution

* py

  ```py
  def isUgly(self, n: int) -> bool:
    for p in 2, 3, 5:
      while n % p == 0 < n:
        n //= p
    return n == 1
  ```
