# [LC_repeated-substring-pattern](https://leetcode.com/problems/repeated-substring-pattern)

```en
Given string s, check if it can be constructed by taking substring of it and appending 1+ copies of substring together
```

```txt
Input: s = "abab"
Output: true  # "ab" twice.

Input: s = "aba"
Output: false

Input: s = "abcabcabcabc"
Output: true  # "abc" four times or substring "abcabc" twice
```

## Solution

* cpp

  ```cpp
  bool repeatedSubstringPattern(string s) {
    return (s + s).find(s, 1) < s.size();
  }
  ```

* py

  ```py
  def repeatedSubstringPattern(self, s: str) -> bool:
    return s in (2 * s)[1:-1]
  ```
