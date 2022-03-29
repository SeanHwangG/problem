```py
def preimageSizeFZF(self, K):
  def f(x):
    return 0 if x < 5 else f(x // 5) + x // 5
  l, r = 0, 5 * (K + 1)
  while l < r:
    m = (r - l) // 2 + l
    if f(m) < K:
      l = m + 1
    else:
      r = m
  return 5 if f(l) == K else 0
```
