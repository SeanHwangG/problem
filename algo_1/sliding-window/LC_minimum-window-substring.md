# [LC_minimum-window-substring](https://leetcode.com/problems/minimum-window-substring)

* en

  ```en
  Given strs s and t, return min window substring of s, ST every char in t (including duplicates) is included in window
  If there is no such substring, return the empty string ""
  ```

* tc

  ```tc
  Input: s = "ADOBECODEBANC", t = "ABC"
  Output: "BANC"

  Input: s = "a", t = "aa"
  Output: ""
  ```

## Solution

* py

  ```py
  def minWindow(self, s, t):
    need, missing = Counter(t), len(t)
    i = l = r = 0
    for j, c in enumerate(s, 1):
      missing -= need[c] > 0
      need[c] -= 1
      if not missing:
        while i < j and need[s[i]] < 0:
          need[s[i]] += 1
          i += 1
        if not r or j - i <= r - l:
          l, r = i, j
    return s[l:r]
  ```
