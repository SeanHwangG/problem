{% tabs %}{% tab title='LC_407.py' %}

* Enqueuing all cells on the outer edges of the input matrix
* Time; O(mnlog(mn))
* Space; O(mn)

```py
def trapRainWater(self, hm: List[List[int]]) -> int:
  if not hm or not hm[0]: return 0
  m, n, res = len(hm), len(hm[0]), 0
  heap = list(set([(hm[i][j], i, j) for i in range(m) for j in [0, n - 1]] +
                  [(hm[i][j], i, j) for j in range(n) for i in [0, m - 1]]))
  heapq.heapify(heap)
  seen = {(x, y) for h, x, y in heap}
  while heap:
    h, x, y = heapq.heappop(heap)
    for xx, yy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
      if m > xx >= 0 <= yy < n and (xx, yy) not in seen:
        seen.add((xx, yy))
        res += max(0, h - hm[xx][yy])
        heapq.heappush(heap, (max(h, hm[xx][yy]), xx, yy))
  return res
```

{% endtab %}{% endtabs %}
