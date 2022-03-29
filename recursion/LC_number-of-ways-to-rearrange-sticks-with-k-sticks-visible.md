```py
@lru_cache(None)
def rearrangeSticks(self, n: int, k: int) -> int:
  if k < 0 or n == 0: return k == 0
  return (self.rearrangeSticks(n - 1, k) * (n - 1) + self.rearrangeSticks(n - 1, k - 1)) % int(1e9 + 7)
```
