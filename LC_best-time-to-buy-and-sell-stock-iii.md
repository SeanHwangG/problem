```cpp
int maxProfit(vector<int>& v, int N = 2) {
  int M = v.size();
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
