# [LC_permutation-in-string](https://leetcode.com/problems/permutation-in-string)

Given two strings s1 and s2, return true if s2 contains the permutation of s1.
In other words, one of s1's permutations is the substring of s2.

```txt
Input: s1 = "ab", s2 = "eidbaooo"
Output: true  # s2 contains one permutation of s1 ("ba").
```

## Solution

```py
def checkInclusion(self, s1: str, s2: str) -> bool:
  k = len(s1)
  d1, d2 = Counter(s1), Counter(s2[:k])
  if d1 == d2:
    return True

  for i in range(len(s2) - k):
    if d2[s2[i]] == 1:
      del d2[s2[i]]
    elif d2[s2[i]] > 1:
      d2[s2[i]] -= 1
    d2[s2[i + k]] += 1
    if d1 == d2:
      return True

  return False
```
