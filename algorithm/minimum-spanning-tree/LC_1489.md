{% tabs %}{% tab title='LC_1489.md' %}

* Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges
* edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi
* Find all the critical and pseudo-critical edges in given graph's minimum spanning tree (MST) in any order
* An MST edge whose deletion from graph would cause MST weight to increase is called a critical edge
* On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all

```txt
Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
```

{% endtab %}{% tab title='LC_1489.py' %}

```py
def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
  def kruskal(ban = None, force = None):
    p = {}
    def find(x):
      p.setdefault(x, x)
      if x != p[x]:
        p[x] = find(p[x])
      return p[x]

    def union(x, y):
      p[find(x)] = find(y)

    if force: union(force[0], force[1])

    total, c = 0, 1
    for i, (x, y, w) in edges:
      if i == ban: continue
      if find(x) != find(y) or (x, y) == force:
        union(x, y)
        total += w
        c += 1
      if c == n or total > init: break
    return total if c == n else inf

  edges = sorted(enumerate(edges), key=lambda x: x[1][2])
  res, init = [[], []], inf
  init = kruskal()
  for i, (x, y, w) in edges:
    if kruskal(i) > init:
      res[0].append(i)
    elif kruskal(None, (x, y)) == init:
      res[1].append(i)
  return res
```

{% endtab %}{% endtabs %}
