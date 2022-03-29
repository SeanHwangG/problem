* Time: O(N^2)
* Space: O(N^2)

```py
def pathsWithMaxScore(self, G: List[str]) -> List[int]:
  N, MOD = len(G), 10**9 + 7
  dp = [[[-10**5, 0] for j in range(N + 1)] for i in range(N + 1)]
  dp[N - 1][N - 1] = [0, 1]
  for r in range(N)[::-1]:
    for c in range(N)[::-1]:
      if G[r][c] in 'XS': continue
      for nr, nc in [[nr, nc + 1], [nr + 1, nc], [nr + 1, nc + 1]]:
        if dp[r][c][0] < dp[nr][nc][0]:
          dp[r][c] = [dp[nr][nc][0], 0]
        if dp[r][c][0] == dp[nr][nc][0]:
          dp[r][c][1] += dp[nr][nc][1]
      dp[r][c][0] += int(G[r][c]) if r or c else 0
  return [dp[0][0][0] if dp[0][0][1] else 0, dp[0][0][1] % MOD]
```
