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
