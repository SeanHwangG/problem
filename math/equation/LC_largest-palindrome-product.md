# [LC_largest-palindrome-product](https://leetcode.com/problems/largest-palindrome-product)

```en
Given integer n, return largest palindromic integer that can be represented as product of two n-digits ints
Return it modulo 1337
```

```txt
Input: n = 2
Output: 987  # 99 x 91 = 9009, 9009 % 1337 = 987
```

## Solution

* py

  ```py
  def largestPalindrome(self, n):  # 10 ^ (2n) - 10 ^ n * (x + y) + xy = 10 ^ n * (10 ^ n - (x + y)) + xy
    if n == 1: return 9
    for z in range(2, 2 * (9 * 10 ** n) - 1):  # z = x + y
      left, right = 10 ** n - z, int(str(left)[::-1]) # left = 10 ^ n - (x+y) / right = xy
      root_1, root_2 = 0, 0

      if z ** 2 - 4 * right < 0:
        continue
      else:
        root_1 = 1 / 2 * (z + (z ** 2 - 4 * right) ** 0.5)
        root_2 = 1 / 2 * (z - (z ** 2 - 4 * right) ** 0.5)
        if root_1.is_integer() or root_2.is_integer():
          return (10 ** n * left + right) %1337
  ```
