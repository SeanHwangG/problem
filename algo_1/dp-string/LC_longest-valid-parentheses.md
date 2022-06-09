# [LC_longest-valid-parentheses](https://leetcode.com/problems/longest-valid-parentheses)

* en

  ```en
  Given a string containing just characters '(' and ')', find length of longest valid parentheses substring
  ```

* tc

  ```tc
  Input: s = "(()"
  Output: 2  # "()".

  Input: s = ")()())"
  Output: 4  # "()()".
  ```

## Solution

* py

  ```py
  def longestValidParentheses(self, s):
    dp = [0] * (len(s) + 1)
    for i in range(len(s) - 2, -1, -1):
      j = i + 1 + dp[i + 1]
      if s[i] == "(" and j < len(s) and s[j] == ")":
        dp[i] = dp[i + 1] + dp[j + 1] + 2
    return max(dp)
  ```
