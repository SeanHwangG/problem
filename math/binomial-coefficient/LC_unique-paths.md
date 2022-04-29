# [LC_unique-paths](https://leetcode.com/problems/unique-paths)

Robot is located at the top-left corner of a m x n grid, can move either down or right
How many possible unique paths are there to the bottom-right corner of the grid?

```txt
Input: m = 7, n = 3
Output: 28
```

## Solution

```py
from math import comb
def uniquePaths(self, m: int, n: int) -> int:
  return comb(m + n - 2, m - 1)
```
