# [LC_regular-expression-matching](https://leetcode.com/problems/regular-expression-matching)

```en
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character
'*' Matches zero or more of the preceding element
Matching should cover the entire input string (not partial)
```

```txt
Input: s = "aab", p = "c*a*b"
Output: true
```

## Solution

* py

  ```py
  @lru_cache(None)
  def isMatch(self, s, p):
    if not p: return not s
    if not s: return len(p) > 1 and p[1] == '*' and self.isMatch(s, p[2:])
    matched = (p[0] == '.' or p[0] == s[0])
    if len(p) > 1 and p[1] == '*':
      return (matched and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
    return matched and self.isMatch(s[1:], p[1:])
  ```
