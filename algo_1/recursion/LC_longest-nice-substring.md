# [LC_longest-nice-substring](https://leetcode.com/problems/longest-nice-substring)

```en
String s is nice if, for every letter of the alphabet that s contains, it appears both in upperc and lowercase
Given a string s, return the longest substring of s that is nice
If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string
```

```txt
Input: s = "YazaAay"
Output: "aAa"
```

## Solution

* py

  ```py
  def longestNiceSubstring(self, s: str) -> str:
    if not s: return ""
    ss = set(s)
    for i, c in enumerate(s):
      if c.swapcase() not in ss:
        s0 = self.longestNiceSubstring(s[:i])
        s1 = self.longestNiceSubstring(s[i+1:])
        return max(s0, s1, key=len)
    return s
  ```
