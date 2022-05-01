# [LC_wildcard-matching](https://leetcode.com/problems/wildcard-matching)

Given input string (s) and pattern (p), implement wildcard pattern matching with support for '?' and '*'

```txt
Input: s = "adceb", p = "*a*?"
Output: true
```

## Solution

* Time: O(N + M)
* Space: O(1)

* cpp

  ```cpp
  class Solution {
  public:
    bool isMatch(string s, string p) {
      int i = 0, j = 0;
      int m = s.length(), n = p.length();
      int last_match = -1, starj = -1;
      while (i < m){
        if (j < n && (s[i] == p[j] || p[j] == '?')){
          i++; j++;
        }
        else if (j < n && p[j] == '*'){
          starj = j;
          j++;
          last_match = i;
        }
        else if (starj != -1){
          j = starj + 1;
          last_match++;
          i = last_match;
        }
        else return false;
      }
      while (p[j] == '*' && j <n) j++;
      return j == n;
    }
  };
  ```

* py

  ```py
  # Time / Space : O(m * n)
  def isMatch(self, s, p):
    length = len(s)
    if len(p) - p.count('*') > length:
      return False
    dp = [True] + [False]*length
    for i in p:
      if i != '*':
        for n in reversed(range(length)):
          dp[n+1] = dp[n] and (i == s[n] or i == '?')
      else:
        for n in range(1, length+1):
          dp[n] = dp[n-1] or dp[n]
      dp[0] = dp[0] and i == '*'
    return dp[-1]
  ```
