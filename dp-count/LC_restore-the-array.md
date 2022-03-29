```py
def numberOfArrays(self, s: str, k: int) -> int:
  N, s = len(s), [*map(int, s)] + [math.inf]
  dp = [0] * N + [1]
  for i in range(N - 1, -1, -1):
    num, j = s[i], i + 1
    while 1 <= num <= k and j < N + 1:
      dp[i] = (dp[i] + dp[j]) % 1000000007
      num = 10 * num + s[j]
      j += 1
  return dp[0]
```
