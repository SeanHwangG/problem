* Time; O(N)

```py
def constrainedSubsetSum(self, dp: List[int], k: int) -> int:
  dq = deque()  # stores dp[i - k], dp[i - k + 1], .., dp[i - 1] whose values are larger than 0 in decreasing order
  for i in range(len(dp)):
    dp[i] += dq[0] if dq else 0  # maximum result if last element is dp[i]
    while len(dq) and dp[i] > dq[-1]:
      dq.pop()
    if dp[i] > 0:
      dq.append(dp[i])
    if i >= k and dq and dq[0] == dp[i - k]:  # Don't need dp[i - k] when computing dp[i + 1], to satisfy j - i <= k
      dq.popleft()
  return max(dp)
```
