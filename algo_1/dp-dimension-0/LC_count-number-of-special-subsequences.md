# [LC_count-number-of-special-subsequences](https://leetcode.com/problems/count-number-of-special-subsequences)

* en

  ```en
  Sequence is special if it consists of + number of 0s, followed by a + number of 1s, then + number of 2s
  For example, [0,1,2] and [0,0,1,1,1,2] are special.
  In contrast, [2,1,0], [1], and [0,1,2,0] are not special.
  Given array nums (only integers 0, 1, 2), return the number of different subsequences that are special MOD10^9 + 7
  ```

* tc

  ```tc
  Input: nums = [0,1,2,2]
  Output: 3  # The special subsequences are [0,1,2,2], [0,1,2,2], and [0,1,2,2].
  ```

## Solution

* py

  ```py
  def countSpecialSubsequences(self, A):
    dp = [1, 0, 0, 0]
    for a in A:
      dp[a + 1] += dp[a] + dp[a + 1]
    return dp[-1] % (10**9 + 7)
  ```
