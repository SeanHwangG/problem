```py
def minimumCost(self, N: int, connections: List[List[int]]) -> int:
  def find(city):
    if parent[city] != city:
      parent[city] = find(parent[city])
    return parent[city]

  def union(c1, c2):
    root1, root2 = find(c1), find(c2)
    if root1 == root2:
      return False
    parent[root2] = root1
    return True

  parent = {city: city for city in range(1, N + 1)}
  total = 0
  for city1, city2, cost in sorted(connections, key=lambda x: x[2]):
    if union(city1, city2):  # [3B]
      total += cost
  root = find(N)
  return total if all(root == find(city) for city in range(1, N + 1)) else -1
```
