```py
def maxChunksToSorted(self, A):
  res, s1, s2 = 0, 0, 0
  for a, b in zip(A, sorted(A)):
    s1 += a
    s2 += b
    res += s1 == s2
  return res
```
