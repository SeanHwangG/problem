# [LC_number-of-restricted-paths-from-first-to-last-node](https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node)

* en

  ```en
  Given an undirected weighted connected graph
  with a positive integer n which denotes that graph has n nodes labeled from 1 to n, and edges= [ui, vi, weighti]
  A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start and zk = end
  there is an edge between zi and zi+1 where 0 <= i <= k-1
  The distance of path is the sum of the weights on the edges of the path
  Let distToLastNode(x) denote the shortest distance of a path between node n and node x
  Restricted path is path that also satisfies that distToLastNode(zi) > distToLastNode(zi+1) where 0 <= i <= k-1
  Return # restricted paths from node 1 to node n modulo 10 ** 9 + 7
  ```

* tc

  ```tc
  Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
  Output: 3
  ```

## Solution

* py

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
