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
