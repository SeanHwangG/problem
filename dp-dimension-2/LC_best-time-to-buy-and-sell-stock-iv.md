```cpp
int maxProfit(int N, vector<int>& v) {
  int M = v.size();
  N = min(N, M / 2);
  if (M == 0) return 0;
  vector<vector<int>> dp(N + 1, vector<int>(M));
  for (int i = 1; i <= N; i++) {
    int mx = -v[0];
    for (int j = 1; j < M; j++) {
      dp[i][j] = max(dp[i][j - 1], mx + v[j]);
      mx = max(mx, dp[i - 1][j - 1] - v[j]);
    }
  }
  return dp[N][M - 1];
}
```

```py
# O(kn)
def maxProfit(self, k, prices):
  if not prices:
    return 0
  profits = [0]*len(prices)
  for j in range(k):
    preprofit = 0
    for i in range(1,len(prices)):
      profit = prices[i] - prices[i-1]
      preprofit = max(preprofit+profit, profits[i])
      profits[i] = max(profits[i-1], preprofit)
  return profits[-1]
```
