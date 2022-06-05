# [LC_palindrome-partitioning-ii](https://leetcode.com/problems/palindrome-partitioning-ii)

```en
Given a string s, partition s such that every substring of partition is a palindrome
Return minimum cuts needed for a palindrome partitioning of s
```

```txt
Input: s = "aab"
Output: 1
```

## Solution

* Generate 2d palindrome table with l index and r indices (N^2 space)
* dp[n] stores the minimum number of cuts s[0: n] (N space)
* Time, Space; O(N^2), O(N)

* py

  ```py
  def minCut(self, s: str) -> int:
    dp = list(range(-1, len(s)))
    for m in range(1, len(s)):
      for l, r in (m, m), (m - 1, m):
        while l >= 0 and r < len(s) and s[l] == s[r]:
          dp[r + 1] = min(dp[r + 1], dp[l] + 1)
          l -= 1
          r += 1
    return dp[-1]
  ```
