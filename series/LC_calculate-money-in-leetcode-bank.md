```py
def totalMoney(self, n: int) -> int:
  k, r = divmod(n, 7)
  return 28 * k + k * (k - 1) // 2 * 7 + (1 + r) * r // 2 + k * r
```
