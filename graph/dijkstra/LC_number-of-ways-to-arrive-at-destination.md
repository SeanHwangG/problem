# [LC_number-of-ways-to-arrive-at-destination](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination)

* en

  ```en
  City consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections
  You can reach any intersection from any other intersection and that there is at most one road between any two intersections
  Given n, 2D array roads where roads[i] = [ui, vi, timei] is a road between ui and vi that takes timei minutes to travel
  Gow many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time
  Return number of ways modulo 10^9 + 7 you can arrive at your destination in the shortest amount of time
  ```

* tc

  ```tc
  Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
  Output: 4

  Input: n = 2, roads = [[1,0,10]]
  Output: 1
  ```

## Solution

* py

  ```py
  def countPaths(self, n: int, roads: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u, v, time in roads:
      graph[u].append([v, time])
      graph[v].append([u, time])

    def dijkstra(src):
      dist = [math.inf] * n
      ways, pq = [0] * n, [(0, src)]  # dist, src
      dist[src], ways[src] = 0, 1
      while pq:
        d, u = heappop(pq)
        if dist[u] < d: continue  # Skip if `d` is not updated to latest version!
        for v, time in graph[u]:
          if dist[v] > d + time:
            dist[v], ways[v] = d + time, ways[u]
            heappush(pq, (dist[v], v))
          elif dist[v] == d + time:
            ways[v] = (ways[v] + ways[u]) % 1_000_000_007
      return ways[n - 1]

    return dijkstra(0)
  ```
