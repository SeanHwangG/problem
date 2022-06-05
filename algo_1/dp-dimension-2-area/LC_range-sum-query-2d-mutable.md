# [LC_range-sum-query-2d-mutable](https://leetcode.com/problems/range-sum-query-2d-mutable)

```en
Update value of a cell in matrix.
Calculate sum of element of matrix inside rectangle defined by its upper left (r1, c1) and lower right (r2, c2)
```

```txt
Input:
["NumMatrix", "sumRegion", "update", "sumRegion"]
[[[[3, 0, 1, 4, 2],
   [5, 6, 3, 2, 1],
   [1, 2, 0, 1, 5],
   [4, 1, 0, 1, 7],
   [1, 0, 3, 0, 5]]],
[2, 1, 4, 3],
[3, 2, 2],
[2, 1, 4, 3]]

Output: [null, 8, null, 10]
```

## Solution

* py

  ```py
  class NumMatrix(object):
    def __init__(self, G):
      for row in G:
        for col in range(1, len(row)):
          row[col] += row[col - 1]
      self.G = G

    def update(self, row, col, val):
      original = self.G[row][col]
      if col != 0:
        original -= self.G[row][col - 1]

      for y in range(col, len(self.G[0])):
        self.G[row][y] += val - original

    def sumRegion(self, row1, col1, row2, col2):
      ret = 0
      for x in range(row1, row2 + 1):
        ret += self.G[x][col2]
        if col1 != 0:
          ret -= self.G[x][col1-1]
      return ret
  ```
