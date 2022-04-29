# [LC_find-and-replace-in-string](https://leetcode.com/problems/find-and-replace-in-string)

Given 0-indexed string s that you must perform k replacement operations on
Replacement operations are given as three 0-indexed parallel array, index, source, target, all of length k
To complete the ith replacement operation:
  Check if the substring sources[i] occurs at index indices[i] in the original string s
  If it does not occur, do nothing
  Otherwise if it does occur, replace that substring with targets[i]

```txt
Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"

Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
```

## Solution

* py

  ```py
  def findReplaceString(self, S, indexes, sources, targets):
    for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
      S = S[:i] + t + S[i + len(s):] if S[i:i + len(s)] == s else S
    return S
  ```
