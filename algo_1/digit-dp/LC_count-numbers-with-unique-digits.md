# [LC_count-numbers-with-unique-digits](https://leetcode.com/problems/count-numbers-with-unique-digits)

* en

  ```en
  Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10^n
  ```

* tc

  ```tc
  Input: n = 2
  Output: 91  # excluding 11, 22
  ```

## Solution

* py

  ```py
  def countNumbersWithUniqueDigits(self, n: int) -> int:
    res, prev = 10, 9
    for i in range(1, n):
      prev *= 10 - i
      res += prev
    return n and res or 1
  ```
