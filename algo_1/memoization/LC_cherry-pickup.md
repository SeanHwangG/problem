# [LC_cherry-pickup](https://leetcode.com/problems/cherry-pickup)

Given an n x n grid representing a field of cherries, each cell is one of three possible integers.
  0 means the cell is empty, so you can pass through,
  1 means the cell contains a cherry that you can pick up and pass through, or
  -1 means the cell contains a thorn that blocks your way.
Return maximum number of cherries you can collect by following rules below:
  Starting at (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with 0/1)
  After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells
  When passing through a path cell containing a cherry, you pick it up, and cell becomes an empty cell 0
  If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected

```txt
Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
Output: 5

Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
Output: 0
```

## Solution

```py
class Solution:
  def cherryPickup(self, G):
    N = len(G)
    v = lambda i, j: 0 <= i < N and 0 <= j < N and G[i][j] != -1

    @lru_cache(None)
    def dfs(a, b, c, d):
      if a == b == c == d == N - 1:
        return G[N - 1][N - 1]
      if not (v(a, b) and v(c, d)):
        return -1e9
      return max(dfs(m, n, p, q) for (m, n),
              (p, q) in product([(a + 1, b), (a, b + 1)], [(c + 1, d), (c, d + 1)])) + G[a][b] + G[c][d] * (a != c)

    return max(dfs(0, 0, 0, 0), 0)
```
