# [LC_longest-increasing-path-in-a-matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix)

* en

  ```en
  Given an m x n integers matrix, return the length of the longest increasing path in matrix
  ```

* tc

  ```tc
  Input: matrix =
    [[9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]]
  Output: 4
  ```

## Solution

* py

  ```py
  def longestIncreasingPath(self, G: List[List[int]]) -> int:
    @lru_cache(None)
    def dfs(x, y):
      length = 1
      for r, c in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
        if 0 <= r < len(G) and 0 <= c < len(G[0]) and G[x][y] < G[r][c]:
          length = max(length, dfs(r, c) + 1)
      return length
    if not any(G): return 0
    return max(dfs(i, j) for i in range(len(G)) for j in range(len(G[0])))
  ```
