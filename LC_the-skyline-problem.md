{% tabs %}{% tab title='LC_218.py' %}

```py
from heapq import heappush, heappop
def getSkyline(self, buildings):
  events = [(L, -H, R) for L, R, H in buildings]  # add start, end building (with 0 height), sort events in l->ri
  events += list({(R, 0, 0) for _, R, _ in buildings})
  events.sort()

  res = [[0, 0]]  # result, [x, height]
  live = [(0, float("inf"))]  # heap, [-height, ending position]
  for pos, negH, R in events:
    while live[0][1] <= pos: heappop(live) # 1, pop buildings that are already ended
      if negH: heappush(live, (negH, R)) # 2, if it's start-building event, make building alive
      if res[-1][1] != -live[0][0]: # 3, if previous keypoint height != current highest height, edit result
        res += [[pos, -live[0][0]]]
  return res[1:]
```

{% endtab %}{% endtabs %}
