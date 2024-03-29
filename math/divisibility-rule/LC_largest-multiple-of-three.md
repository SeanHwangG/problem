# [LC_largest-multiple-of-three](https://leetcode.com/problems/largest-multiple-of-three)

* en

  ```en
  Given int array of digits, return largest multiple of three that can be formed by concatenating some given digits
  Since the answer may not fit in an integer data type, return the answer as a string
  If there is no answer return an empty string
  ```

* tc

  ```tc
  Input: digits = [8,1,9]
  Output: "981"
  ```

## Solution

* py

  ```py
  def largestMultipleOfThree(self, digits: List[int]) -> str:
    dp = [-1, -1, -1]
    for a in sorted(digits)[::-1]:
      for x in dp[:] + [0]:
        y = x * 10 + a
        dp[y % 3] = max(dp[y % 3], y)
    return str(dp[0]) if dp[0] >= 0 else ""
  ```
