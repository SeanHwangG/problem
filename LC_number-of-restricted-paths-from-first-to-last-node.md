{% tabs %}{% tab title='LC_1786.py' %}

```py
class Solution:
  def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
    if n == 1: return 0
    graph = defaultdict(list)
    for u, v, w in edges:
      graph[u].append((w, v))
      graph[v].append((w, u))

    dist2n = [inf] * (n) + [0]
    minHeap = [(0, n)]
    while minHeap:
      d, u = heappop(minHeap)
      for w, v in graph[u]:
        if dist2n[v] > dist2n[u] + w:
          dist2n[v] = dist2n[u] + w
          heappush(minHeap, (dist2n[v], v))

    @lru_cache(None)
    def dfs(src):
      if src == n: return 1
      ans = 0
      for _, nei in graph[src]:
        if dist2n[src] > dist2n[nei]:
          ans = (ans + dfs(nei)) % 1000000007
      return ans

    return dfs(1)
```

{% endtab %}{% endtabs %}
