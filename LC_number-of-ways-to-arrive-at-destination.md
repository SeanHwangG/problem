{% tabs %}{% tab title='LC_1976.py' %}

```py
def countPaths(self, n: int, roads: List[List[int]]) -> int:
  graph = defaultdict(list)
  for u, v, time in roads:
    graph[u].append([v, time])
    graph[v].append([u, time])

  def dijkstra(src):
    dist = [math.inf] * n
    ways, pq = [0] * n, [(0, src)]  # dist, src
    dist[src], ways[src] = 0, 1
    while pq:
      d, u = heappop(pq)
      if dist[u] < d: continue  # Skip if `d` is not updated to latest version!
      for v, time in graph[u]:
        if dist[v] > d + time:
          dist[v], ways[v] = d + time, ways[u]
          heappush(pq, (dist[v], v))
        elif dist[v] == d + time:
          ways[v] = (ways[v] + ways[u]) % 1_000_000_007
    return ways[n - 1]

  return dijkstra(0)
```

{% endtab %}{% endtabs %}
