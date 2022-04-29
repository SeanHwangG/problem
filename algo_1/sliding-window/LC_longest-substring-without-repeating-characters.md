# [LC_longest-substring-without-repeating-characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)

Given string s, find the length of the longest substring without repeating characters

```txt
Input: s = "abcabcbb"
Output: 3  # abc
```

## Solution

```py
def lengthOfLongestSubstring(self, s: str) -> int:
  used = {}
  max_length = l = 0
  for r, c in enumerate(s):
    if c in used and l <= used[c]:
      l = used[c] + 1
    else:
      max_length = max(max_length, r - l + 1)
    used[c] = r
  return max_length
```
