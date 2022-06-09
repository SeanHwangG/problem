# [LC_sqrtx](https://leetcode.com/problems/sqrtx)

* en

  ```en
  Implement sqrt function
  ```

* tc

  ```tc
  Input: x = 4
  Output: 2
  ```

## Solution

* Newton's method
  * $$ x_{k + 1} = \frac{1}{2} (x_k+\frac{n}{x_k}), k ≥ 0, x_0 > 0 $$

* py

  ```py
  def mySqrt(self, x: int) -> int:
    r = x
    while r * r > x:
      r = (r + x / r) / 2
    return r
  ```
