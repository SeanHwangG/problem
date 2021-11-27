{% tabs %}{% tab title='LC_1192.md' %}

* There are n servers numbered from 0 to n - 1 connected by undirected server connections forming network
  * connections[i] = [ai, bi] represents a connection between servers ai and bi
* Any server can reach other servers directly or indirectly through the network
* A critical connection is a connection that, if removed, will make some servers unable to reach some other server
* Return all critical connections in the network in any order

```txt
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
```

{% endtab %}{% tab title='LC_1192.py' %}

* Time: O(E+V)

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
