# [LC_distinct-subsequences](https://leetcode.com/problems/distinct-subsequences)

* en

  ```en
  Given two strings s and t, return the number of distinct subsequences of s which equals t
  ```

* tc

  ```tc
  Input: s = "rabbbit", t = "rabbit"
  Output: 3
  ```

## Solution

* py

  ```py
  def numDistinct(self, s: str, t: str) -> int:
    dp = [[1] * (len(s)+1)] + [[0] * (len(s)+1) for y in range(len(t))]
    for j in range(1, len(t)+1):
      for i in range(1, len(s)+1):
        dp[j][i] += dp[j-1][i-1] + dp[j][i-1] if s[i-1] == t[j-1] else dp[j][i-1]
    return dp[-1][-1]
  ```
