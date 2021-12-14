{% tabs %}{% tab title='LC_743.py' %}

* Time: O(VE)
* Space: O(N)

```py
def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
  dist = [float("inf") for _ in range(N)]
  dist[K - 1] = 0
  for _ in range(N - 1):
    for u, v, w in times:
      if dist[u - 1] + w < dist[v - 1]:
        dist[v - 1] = dist[u - 1] + w
  return max(dist) if max(dist) < float("inf") else -1
```

{% endtab %}{% endtabs %}
