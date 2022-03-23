```py
from functools import lru_cache

def canCross(self, stones):
  goal, stones = stones[-1], set(stones)

  @lru_cache(None)
  def bt(cur, speed):
    if cur > goal or cur < 0 or speed <= 0 or cur not in stones:
      return False
    return cur == goal or any(bt(cur + ns, ns) for ds in (speed - 1, speed, speed + 1) if cur + ns in stones)

  return bt(1, 1)
```
