```py
def minStickers(self, stickers: List[str], target: str) -> int:
  @lru_cache(None)
  def query(s):
    if not s: return 0
    c, ans = Counter(s), float('inf')
    for st in [Counter(s) for s in stickers]:
      if s[-1] not in st: continue
      ns = ""
      for k, v in (c - st).items():
        ns += k * v
      ans = min(ans, query(ns) + 1)
    return ans
  return query(target) if query(target) != float('inf') else -1
```
