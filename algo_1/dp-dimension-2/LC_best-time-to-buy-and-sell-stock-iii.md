# [LC_best-time-to-buy-and-sell-stock-iii](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii)

Find maximum profit you can achieve. May complete at most two transactions
Cannot engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again)

```txt
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
```

## Solution

* cpp

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
