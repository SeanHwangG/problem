# [LC_unique-paths-ii](https://leetcode.com/problems/unique-paths-ii)

* en

  ```en
  Robot is located at the top-left corner of a m x n grid
  The robot can only move either down or right, trying to reach the bottom-right corner of the grid
  Now consider if some obstacles are added to the grids. How many unique paths would there be?
  ```

* tc

  ```tc
  Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
  Output: 2
  ```

## Solution

* Time; O(N^2)
* Space; O(N)

* py

  ```py
  def uniquePathsWithObstacles(self, G: List[List[int]]) -> int:
    if not G:
      return
    cur = [0] * len(G[0])
    cur[0] = 1 - G[0][0]
    for i in range(1, len(G[0])):
      cur[i] = cur[i-1] * (1 - G[0][i])
    for i in range(1, len(G)):
      cur[0] *= (1 - G[i][0])
      for j in range(1, len(G[0])):
        cur[j] = (cur[j-1] + cur[j]) * (1 - G[i][j])
    return cur[-1]

  ```
