# [LC_super-egg-drop](https://leetcode.com/problems/super-egg-drop)

* en

  ```en
  Given K eggs, and you have access to a building with N floors from 1 to N
  What is the minimum number of moves that you need to know with certainty what F
  ```

* tc

  ```tc
  Input: k = 2, n = 6
  Output: 3
  ```

## Solution

* Time; O(KlogN)
* Space; O(K)

* cpp

  ```cpp
  int superEggDrop(int K, int N) {
    vector<int> dp(K + 1, 0);
    int m;
    for (m = 0; dp[K] < N; m++)
      for (int k = K; k > 0; --k)
        dp[k] += dp[k - 1] + 1;
    return m;
  }
  ```

* py

  ```py
  def superEggDrop(self, K: int, N: int) -> int:
    dp = [[0] * (K + 1) for i in range(N + 1)]
    for m in range(1, N + 1):
      for k in range(1, K + 1):
        dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
      if dp[m][K] >= N: return m
  ```
