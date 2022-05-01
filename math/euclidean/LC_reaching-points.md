# [LC_reaching-points](https://leetcode.com/problems/reaching-points)

Given ints sx, sy, tx, ty, return if it's possible to convert (sx, sy) to (tx, ty) with some operations
The allowed operation on some point (x, y) is to convert it to either (x, x + y) or (x + y, y)

```txt
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: true  # (1, 1) -> (1, 2) / (1, 2) -> (3, 2) / (3, 2) -> (3, 5)
```

## Solution

* ![LC_780](images/20210729_232232.png)

* py

  ```py
  def reachingPoints(self, sx, sy, tx, ty):
    if tx < sx or ty < sy:
      return False
    if sx == tx:
      return (ty - sy) % sx == 0
    if sy == ty:
      return (tx - sx) % sy == 0

    if tx > ty:
      return self.reachingPoints(sx, sy, tx % ty, ty)
    else:
      return self.reachingPoints(sx, sy, tx, ty % tx)
  ```
