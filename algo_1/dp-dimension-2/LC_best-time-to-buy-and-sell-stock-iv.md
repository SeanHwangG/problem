# [LC_best-time-to-buy-and-sell-stock-iv](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv)

* en

  ```en
  Given integer array prices where prices[i] is the price of a given stock on the ith day, and integer k
  Find the maximum profit you can achieve. You may complete at most k transactions
  You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again)
  ```

* tc

  ```tc
  Input: k = 2, prices = [3,2,6,5,0,3]
  Output: 7  #  Buy on day 2 and sell on day 3, profit = 4. Then buy on day 5 and sell on day 6, profit 3
  ```

## Solution

* cpp

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

* py

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
