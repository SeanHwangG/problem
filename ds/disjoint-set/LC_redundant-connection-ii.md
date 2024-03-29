# [LC_redundant-connection-ii](https://leetcode.com/problems/redundant-connection-ii)

* en

  ```en
  Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes
  ```

* tc

  ```tc
  Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
  Output: [4,1]
  ```

## Solution

1. There is no cycle in the graph, but there exist two edges pointing to the same node;
1. There is a cycle, but there do not exist two edges pointing to the same node;
1. There is a cycle, and there exist two edges pointing to the same node.

* py

  ```py
  class UnionFind:
    def __init__(self, n):
      self.parent = list(range(n))

    def find(self, x):
      if self.parent[x] == x:
        return x
      return self.find(self.parent[x])

    def union(self, x, y):
      x, y = self.find(x), self.find(y)
      self.parent[x] = self.parent[y]
      return x != y

  def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
    cand1, cand2, point_to = None, None, {}  # if cycle exists and cand1, cand2 are None, edge that incurs cycle is bad
    for node1, node2 in edges:
      if node2 in point_to:
        cand1, cand2 = point_to[node2], [node1, node2]  # save edges that point to one node
        break
      point_to[node2] = [node1, node2]

    uf = UnionFind(len(edges))
    for node1, node2 in edges:  # pretend the edges are undirected
      if [node1, node2] == cand2: continue  # ignored, if a cycle is detected in the union find process
      if not uf.union(node1 - 1, node2 - 1):
        if cand1: return cand1
        return [node1, node2]
    return cand2
  ```
