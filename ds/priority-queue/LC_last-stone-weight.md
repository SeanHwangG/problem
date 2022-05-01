# [LC_last-stone-weight](https://leetcode.com/problems/last-stone-weight)

Each turn, we choose the two heaviest stones with x, y (x <= y) and smash them together, then
  If x == y, both stones are totally destroyed;
  If x != y, stone of weight x is totally destroyed, and the stone of weight y has new weight y-x
At end, there is at most 1 stone left.  Return the weight of this stone

```txt
Input: [2,7,4,1,8,1]
Output: 1
```

## Solution

* js

  ```js
  const lastStoneWeight = s =>
    1 === s.length ? s[0] : lastStoneWeight(s.sort((a, b) => a - b).concat(s.pop() - s.pop()));
  ```

* py

  ```py
  def lastStoneWeight(self, l: List[int]) -> int:
    l = [-e for e in l]
    heapq.heapify(l)
    while len(l) > 1:
      mx1 = heapq.heappop(l)
      mx2 = heapq.heappop(l)
      if mx1 != mx2:
        heapq.heappush(l, mx1 - mx2)
    return 0 if len(l) == 0 else -l[0]
  ```
