# [LC_dungeon-game](https://leetcode.com/problems/dungeon-game)

* en

  ```en
  Return the knight's minimum initial health so that he can rescue the princess
  ```

* tc

  ```tc
  Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
  Output: 7
  ```

## Solution

* py

  ```py
  def calculateMinimumHP(self, G: List[List[int]]) -> int:
    m, n = len(G), len(G[0])
    dp = [[float("inf")]*(n+1) for _ in range(m+1)]
    dp[m-1][n], dp[m][n-1] = 1, 1

    for i in range(m - 1, -1, -1):
      for j in range(n - 1, -1, -1):
        dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - G[i][j], 1)

    return dp[0][0]
  ```
