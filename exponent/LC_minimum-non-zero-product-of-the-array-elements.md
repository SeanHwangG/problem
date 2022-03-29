```py
def minNonZeroProduct(self, p: int) -> int:
  MOD, mx = int(1e9 + 7), 2 ** p - 1
  return (pow(mx - 1, (mx - 1) // 2, MOD) * (mx)) % MOD
```
