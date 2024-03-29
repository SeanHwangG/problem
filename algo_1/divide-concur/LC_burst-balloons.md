# [LC_burst-balloons](https://leetcode.com/problems/burst-balloons)

* en

  ```en
  Burst gives nums[left] x nums[i] x nums[right] point
  ```

* tc

  ```tc
  Input: nums = [3,1,5,8]
  Output: 167
  ```

## Solution

* py

  ```py
  def maxCoins(self, li):
    li = [1] + li + [1]
    n = len(li)
    dp = [[0] * n for _ in range(n)]        # dp[i][j] coins obtained from balloons between index i and j
    for gap in range(2, n):
      for i in range(n - gap):
        j = i + gap
        for k in range(i+1, j):             # k is last balloon index
          dp[i][j] = max(dp[i][j], li[i] * li[k] * li[j] + dp[i][k] + dp[k][j])
    return dp[0][n-1]
  ```
