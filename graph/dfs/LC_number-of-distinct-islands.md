# [LC_number-of-distinct-islands](https://leetcode.com/problems/number-of-distinct-islands)

Given m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally
Island is considered to be same as another if island can be translated (not rotated or reflected) to equal the other
Return number of distinct islands

```txt
Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1

Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3
```

## Solution

* py

  ```py
  def numDistinctIslands(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    grid.append([0] * n)
    for row in grid: row.append(0)
    def dfs(i,j,path):
      if not grid[i][j]: return ''
      grid[i][j] = 0
      return path + dfs(i - 1, j, 'u') + 'd' + dfs(i + 1, j, 'd') + 'u' +
        dfs(i, j - 1, 'l') + 'r' + dfs(i, j + 1, 'r') + 'l'
    return len({dfs(i, j, '') for i in range(m) for j in range(n) if grid[i][j]})
  ```
