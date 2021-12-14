{% tabs %}{% tab title='LC_210.py' %}

* Time; O(V + E)
* Space; O(V + E)

```py
def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
  G = [[] for i in range(n)]
  degree = [0] * n
  for i, j in prerequisites:
    G[i].append(j)  # Take i before j
    degree[j] += 1
  bfs = [i for i in range(n) if degree[i] == 0]
  for i in bfs:
    for j in G[i]:
      degree[j] -= 1
      if degree[j] == 0:
        bfs.append(j)
  return reversed(bfs) if len(bfs) == n else []
```

{% endtab %}{% endtabs %}
