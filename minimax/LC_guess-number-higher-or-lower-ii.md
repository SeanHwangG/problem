```py
def getMoneyAmount(self, n: int) -> int:
  @lru_cache(maxsize=None)
  def recur(l, r):
    if l >= r: return 0
    return min(i + max(recur(l, i - 1), recur(i + 1, r)) for i in range(l, r + 1))
  return recur(1, n)
```
