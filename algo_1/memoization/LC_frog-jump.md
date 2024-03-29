# [LC_frog-jump](https://leetcode.com/problems/frog-jump)

* en

  ```en
  Given list of stones' positions in sorted ascending order, determine if frog can cross river by landing on last stone
  Initially, frog is on first stone and assumes first jump must be 1 unit
  If frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units
    Frog can only jump in forward direction
  ```

* tc

  ```tc
  Input: stones = [0,1,3,5,6,8,12,17]
  Output: true
  ```

## Solution

* py

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
