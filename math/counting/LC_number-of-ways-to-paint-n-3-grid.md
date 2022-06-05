# [LC_number-of-ways-to-paint-n-3-grid](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid)

```en
Given grid of size n x 3 and paint each cell of grid with one of three colors
Red, Yellow, or Green while making sure that no two adjacent cells have same color
Given n number of rows of grid, return number of ways you can paint this grid, Modulo 10**9 + 7
```

```txt
Input: n = 1
Output: 12

Input: n = 2
Output: 54
```

## Solution

* py

  ```py
  def numOfWays(self, n: int) -> int:
    a121, a123, mod = 6, 6, 10 ** 9 + 7
    for i in range(n - 1):
      a121, a123 = a121 * 3 + a123 * 2, a121 * 2 + a123 * 2
    return (a121 + a123) % mod
  ```
