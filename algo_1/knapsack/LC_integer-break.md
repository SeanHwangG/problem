# [LC_integer-break](https://leetcode.com/problems/integer-break)

Given int n, break it into sum of k positive integers, where k >= 2, and maximize product of those integers
Return maximum product you can get

```txt
Input: n = 10
Output: 36  # 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
```

## Solution

* py

  ```py
  def integerBreak(self, n: int) -> int:
    case = [0, 0, 1, 2, 4, 6, 9]
    if n < 7:
      return case[n]
    dp = case + [0] * (n - 6)
    for i in range(7, n + 1):
      dp[i] = 3 * dp[i - 3]
    return dp[-1]
  ```
