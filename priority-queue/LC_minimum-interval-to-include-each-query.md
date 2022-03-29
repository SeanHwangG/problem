* Time; O(N log N)

```py
def minInterval(self, li: List[List[int]], queries: List[int]) -> List[int]:
  li = sorted(li)[::-1]
  pq, res = [], {}
  for q in sorted(queries):
    while li and li[-1][0] <= q:
      i, j = li.pop()
      if j >= q:
        heapq.heappush(pq, [j - i + 1, j])
    while pq and pq[0][1] < q:
      heapq.heappop(pq)
    res[q] = pq[0][0] if pq else -1
  return [res[q] for q in queries]
```
