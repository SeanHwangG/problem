```py
def nearestPalindromic(self, n: str) -> str:
  l = len(n)
  candidates = set((str(10 ** l + 1), str(10 ** (l - 1) - 1)))  # with different digits width, must be 10...01 or 9...9
  prefix = int(n[:(l + 1) // 2])  # closest must be in middle digit +1, 0, -1, then flip left to right
  for i in map(str, (prefix - 1, prefix, prefix + 1)):
    candidates.add(i + [i, i[:-1]][l & 1][::-1])
  candidates.discard(n)
  return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
```
