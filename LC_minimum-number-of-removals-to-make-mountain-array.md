```py
def minimumMountainRemovals(self, A: List[int]) -> int:
  n = len(A)
  dp, mono = [0] * n, [10**9] * n
  for i in range(n):
    j = bisect_left(mono, A[i])
    mono[j] = A[i]
    dp[i] += j + 1 if j else -n
  mono = [10**9] * n
  for i in range(n - 1, -1, -1):
    j = bisect_left(mono, A[i])
    mono[j] = A[i]
    dp[i] += j if j else -n
  return n - max(dp[1:-1])
```
