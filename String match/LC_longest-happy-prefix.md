# [LC_longest-happy-prefix](https://leetcode.com/problems/longest-happy-prefix)

String is called happy prefix if is non-empty prefix which is also a suffix (excluding itself)
Given a string s, return longest happy prefix of s, empty string "" if no such prefix exists

```txt
Input: s = "level"
Output: "l"

Input: s = "ababab"
Output: "abab"
```

## Solution

```py
def longestPrefix(self, s: str) -> str:
  lps = [0] * len(s)
  for i in range(1, len(s)):
    t = lps[i-1]
    while t and s[t] != s[i]:
      t = lps[t-1]
    if s[t] == s[i]:
      t += 1
    lps[i] = t
  return s[:lps[-1]]
```
