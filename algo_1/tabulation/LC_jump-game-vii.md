# [LC_jump-game-vii](https://leetcode.com/problems/jump-game-vii)

Given a 0-indexed binary string s and two integers minJump and maxJump
Starting at index 0, which is equal to '0', move from index i to index j if the following conditions are fulfilled:
  i + minJump <= j <= min(i + maxJump, s.length - 1), and s[j] == '0'
Return if you can reach index s.length - 1 in s

```txt
Input: s = "011010", minJump = 2, maxJump = 3
Output: true
```

## Solution

* py

  ```py
  def canReach(self, s, minJ, maxJ):
    dp = [c == '0' for c in s]
    pre = 0
    for i in range(1, len(s)):
      if i >= minJ: pre += dp[i - minJ]
      if i > maxJ: pre -= dp[i - maxJ - 1]
      dp[i] &= pre > 0
    return dp[-1]
  ```
