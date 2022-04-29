# [LC_distinct-subsequences-ii](https://leetcode.com/problems/distinct-subsequences-ii)

Count the number of distinct, non-empty subsequences of S

```txt
Input: s = "abc"
Output: 7   # "a", "b", "c", "ab", "ac", "bc", and "abc".
```

## Solution

```py
def distinctSubseqII(self, S):
  res, end = 0, collections.Counter()
  for c in S:
    res, end[c] = res * 2 + 1 - end[c], res + 1
  return res % (10 ** 9 + 7)
```
