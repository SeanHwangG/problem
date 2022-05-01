# [LC_remove-duplicate-letters](https://leetcode.com/problems/remove-duplicate-letters)

Given string s, remove duplicate letters so that every letter appears once and only once
Make sure result is smallest in lexicographical order among all possible results

```txt
Input: s = "cbacdcbc"
Output: "acdb"
```

## Solution

* py

  ```py
  def removeDuplicateLetters(self, s):
    for c in sorted(set(s)):
      suffix = s[s.index(c):]
      if set(suffix) == set(s):
        return c + self.removeDuplicateLetters(suffix.replace(c, ''))
    return ''
  ```
