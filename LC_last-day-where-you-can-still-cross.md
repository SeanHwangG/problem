{% tabs %}{% tab title='LC_1970.py' %}

* Time; O(n * log n)

```py
def latestDayToCross(self, row: int, col: int, A: List[List[int]]) -> int:
  def find(x):
    parents.setdefault(x, x)
    if x != parents[x]:
      parents[x] = find(parents[x])
    return parents[x]
  def union(x, y):
    parents[find(x)] = find(y)
  vis, top, parents = set(), set(), {}
  for r in range(1, row + 1):
    union('l', (r, 1))
    union('r', (r, col))
  for i, (r, c) in enumerate(A):
    vis.add((r, c))
    for nr, nc in [(r + dr, c + dc) for dr in [1, 0, -1] for dc in [1, 0, -1]]:
      if (nr, nc) in vis:
        union((r, c), (nr, nc))
    if find('l') == find('r'):
      return i
```

{% endtab %}{% endtabs %}
