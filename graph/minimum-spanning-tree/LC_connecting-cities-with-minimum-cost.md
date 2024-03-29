# [LC_connecting-cities-with-minimum-cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost)

* en

  ```en
  There are n cities labeled from 1 to n. Given integer n and an array connections
  connections[i] = [xi, yi, costi] indicate that cost of connecting city xi, yi (bidirectional connection) is costi
  Return min cost to connect all n cities ST at least one path between each pair of cities, return -1 if impossible
  ```

* tc

  ```tc
  Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
  Output: 6

  Input: n = 4, connections = [[1,2,3],[3,4,4]]
  Output: -1
  ```

## Solution

* py

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
