# [LC_rearrange-string-k-distance-apart](https://leetcode.com/problems/rearrange-string-k-distance-apart)

Given string s and an integer k, rearrange s such that the same characters are at least distance k from each other
If it's not possible to rearrange the string, return an empty string ""


```txt
Input: s = "aabbcc", k = 3
Output: "abcabc"
```

## Solution

* py

```py
def rearrangeString(self, s: str, k: int) -> str:
  n = len(s)
  if not k:
    return s
  count = Counter(s)
  maxf = max(count.values())
  if (maxf - 1) * k + list(count.values()).count(maxf) > len(s):
    return ""
  res, i = list(s), (n - 1) % k
  for c in sorted(count, key = lambda i: -count[i]):
    for j in range(count[c]):
      res[i] = c
      i += k
      if i >= n:
        i = (i - 1) % k
  return "".join(res)
```
