# [LC_maximal-square](https://leetcode.com/problems/maximal-square)

* en

  ```en
  Find largest square containing only 1's
  ```

* tc

  ```tc
  Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
  Output: 4
  ```

## Solution

* py

  ```py
  def maximalSquare(self, G):
    if len(G) == 0:
      return 0
    n, m, ret, flag = len(G), len(G[0]), 0, 0
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
      for j in range(m):
        if G[i][j] == '1':
          dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j], dp[i][j + 1]) + 1
          ret = max(ret, dp[i + 1][j + 1])

    return ret ** 2
    # with flag
    # for i in range(n):
    #     for j in range(m):
    #         if G[i][j] == '1':
    #             dp[flag][j + 1] = min(dp[flag][j], dp[flag ^ 1][j], dp[flag ^ 1][j + 1]) + 1
    #             ret = max(ret, dp[flag][j + 1])
    #         else:
    #             dp[flag][j + 1] = 0
    #     flag ^= 1
    ```
