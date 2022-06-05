# [LC_number-of-unique-good-subsequences](https://leetcode.com/problems/number-of-unique-good-subsequences)

```en
Given a binary string binary, find number of unique good subsequences of binary MOD 10^9 + 7
Subsequence of binary is considered good if it is not empty and has no leading zeros (with the exception of "0").
```

```txt
Input: binary = "001"
Output: 2

Input: binary = "11"
Output: 2

Input: binary = "101"
Output: 5
```

## Solution

* py

  ```py
  def numberOfUniqueGoodSubsequences(self, b: str) -> int:
    mod = 10**9 + 7
    dp = [0, 0]
    for c in b:
      dp[int(c)] = (sum(dp) + int(c)) % mod
    return (sum(dp) + ('0' in b)) % mod
  ```
