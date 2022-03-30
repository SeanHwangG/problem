```py
def countSpecialSubsequences(self, A):
  dp = [1, 0, 0, 0]
  for a in A:
    dp[a + 1] += dp[a] + dp[a + 1]
  return dp[-1] % (10**9 + 7)
```