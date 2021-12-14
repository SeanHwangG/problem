{% tabs %}{% tab title='LC_1353.py' %}

```py
def maxEvents(self, A):
  A.sort(reverse=1)
  h = []
  res = d = 0
  while A or h:
    if not h: d = A[-1][0]
    while A and A[-1][0] <= d:  # add new events to pq starting on day d
      heapq.heappush(h, A.pop()[1])
    heapq.heappop(h) # greedily attend the event that ends soonest
    res += 1
    d += 1
    while h and h[0] < d:
      heapq.heappop(h)
  return res
```

{% endtab %}{% endtabs %}
