# [LC_stickers-to-spell-word](https://leetcode.com/problems/stickers-to-spell-word)

```en
Spell out given string target by cutting individual letters from your collection of stickers and rearranging them
Use each sticker more than once if you want, and you have infinite quantities of each sticker
Return min # stickers that you need to spell out target. If the task is impossible, return -1
```

```txt
Input: stickers = ["with", "example", "science"], target = "thehat"
Output: 3
```

## Solution

* py

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
