# [LC_powx-n](https://leetcode.com/problems/powx-n)

* en

  ```en
  Implement pow(x, n), which calculates x raised to the power n
  ```

* tc

  ```tc
  Input: 2 3
  Output: 8
  ```

## Solution

* py

  ```py
  def myPow(self, x, n):
    if n < 0:
      x = 1 / x
      n = -n
    pow = 1
    while n:
      if n & 1:
        pow *= x
      x *= x
      n >>= 1
    return pow
  ```
