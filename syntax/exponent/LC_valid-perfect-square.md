# [LC_valid-perfect-square](https://leetcode.com/problems/valid-perfect-square)

```en
Check if a number is square
```

```txt
Input: num = 16
Output: true
```

## Solution

* Newton's method

* py

  ```py
  def isPerfectSquare(self, x: int) -> bool:
    r = x
    while r * r > x:
      r = (r + x // r) // 2
    return r * r == x
  ```
