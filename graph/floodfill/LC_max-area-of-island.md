# [LC_max-area-of-island](https://leetcode.com/problems/max-area-of-island)

* en

  ```en
  Area of an island is the number of cells with a value 1 in the island.
  Return the maximum area of an island in grid. If there is no island, return 0.
  ```

* tc

  ```tc
  Input: grid =
  [[0,0,1,0,0,0,0,1,0,0,0,0,0],
   [0,0,0,0,0,0,0,1,1,1,0,0,0],
   [0,1,1,0,1,0,0,0,0,0,0,0,0],
   [0,1,0,0,1,1,0,0,1,0,1,0,0],
   [0,1,0,0,1,1,0,0,1,1,1,0,0],
   [0,0,0,0,0,0,0,0,0,0,1,0,0],
   [0,0,0,0,0,0,0,1,1,1,0,0,0],
   [0,0,0,0,0,0,0,1,1,0,0,0,0]]
  Output: 6
  ```

## Solution

* py

  ```py
  def maxAreaOfIsland(self, grid):
    m, n = len(grid), len(grid[0])
    def dfs(i, j):
      if 0 <= i < m and 0 <= j < n and grid[i][j]:
        grid[i][j] = 0
        return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
      return 0

    areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
    return max(areas) if areas else 0
  ```
