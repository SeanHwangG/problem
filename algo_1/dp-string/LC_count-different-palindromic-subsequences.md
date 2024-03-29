# [LC_count-different-palindromic-subsequences](https://leetcode.com/problems/count-different-palindromic-subsequences)

* en

  ```en
  Given a string s, find # different non-empty palindromic subsequences in s, and return modulo 10^9 + 7
  ```

* tc

  ```tc
  Input: s = 'bccb'
  Output: 6
  ```

## Solution

* Given l and r index of palindrome, the number is dp[l + 1][r - 1] + 2
* Improve using another two dps instead of index, rindex

* py

  ```py
  def countPalindromicSubsequences(self, S: str) -> int:
    dp = [[0] * len(S) for _ in range(len(S))]
    for size in range(1, len(S) + 1):
      for i in range(len(S) - size + 1):
        for c in "abcd":
          try:
            l, r = S.index(c, i, i + size), S.rindex(c, i, i + size)
            if l == r: dp[i][i + size - 1] += 1
            else:      dp[i][i + size - 1] += dp[l + 1][r - 1] + 2
          except:
            pass
    return dp[0][-1] % 1000000007
  ```
