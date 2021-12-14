{% tabs %}{% tab title='LC_1192.py' %}

* Time; O(E+V)

```py
def dfs(self, u, prev_node, node):
  self.visited.add(node)
  self.low[node] = u

  for v in self.d[node]:
    if v == prev_node:
      continue

    if v not in self.visited:
      self.dfs(u + 1, node, v)  # Propogate to neighbours

    self.low[node] = min(self.low[node], self.low[v])
    if u < self.low[v]:  # Bridge found
      self.res.append([node, v])
def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
  self.d = defaultdict(list)
  for k, v in connections:
    self.d[k].append(v)
    self.d[v].append(k) # undirected

  self.res, self.visited, self.low = [], set(), {}
  self.dfs(0, -1, 0)
  return self.res
```

{% endtab %}{% endtabs %}
