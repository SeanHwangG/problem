# [LC_strange-printer](https://leetcode.com/problems/strange-printer)

* en

  ```en
  Printer can only print sequence of same character each time
  Each turn, printer print new characters starting from and ending at any place and will cover original existing characters
  Given string s, return minimum number of turns printer needed to print it
  ```

* tc

  ```tc
  Input: s = "aba"
  Output: 2  # Print "aaa" first and then print "b"
  ```

## Solution

* py

  ```py
  def strangePrinter(self, S):
    S = re.sub(r'(.)\1*', r'\1', S)
    @lru_cache(None)
    def dp(i, j):
      if i > j: return 0
      ans = dp(i + 1, j) + 1
      for k in range(i + 1, j + 1):
        if S[k] == S[i]:
          ans = min(ans, dp(i, k - 1) + dp(k + 1, j))
      return ans
    return dp(0, len(S) - 1)
  ```
