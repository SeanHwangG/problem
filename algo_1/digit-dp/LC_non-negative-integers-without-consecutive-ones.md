# [LC_non-negative-integers-without-consecutive-ones](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones)

* en

  ```en
  Given + integer n, return # integers in range [0, n] whose binary representations don't contain consecutive one
  ```

* tc

  ```tc
  Input: n = 5
  Output: 5
  ```

## Solution

1. Use fibonacci because 0-10000 is sum of 00000-01111 and 10000-10111
2. If number starts with "11", all int will be smaller than our number, so return a Fibonacci number for n bits
3. If number starts with "10", all int with n - 1 bits will be smaller than our number
    * so, return Fibonacci number for n - 1 bits

* py

  ```py
  def findIntegers(self, n: int) -> int:
    res, x, y, n = 0, 1, 2, n + 1   # 00000-01111 and 10000-10111 so fibonacci
    while n:
      if n & 3 == 3:
        res = 0
      res += x * (n & 1)
      n >>= 1
      x, y = y, x + y
    return res
  ```
