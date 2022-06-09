# [LC_shortest-distance-from-all-buildings](https://leetcode.com/problems/shortest-distance-from-all-buildings)

* en

  ```en
  Given m x n grid grid of values 0, 1, or 2, where:
  0 marks an empty land, 1 marks a building, 2 marks an obstacle
  Build house on an empty land that reaches all buildings in the shortest total travel distance
  ```

* tc

  ```tc
  Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
  Output: 7

  Input: grid = [[1,0]]
  Output: 1
  ```

## Solution

* Start with building, mark all distance

* Time, Space; O(kmn) O(mn)

* py

  ```py
  def shortestDistance(self, grid):
    N, M = len(grid), len(grid[0])

    def next(i, j):
      return [(nr, nc) for nr, nc in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                            if N > nr >= 0 <= nc < M and grid[nr][nc] == target]

    total, target = deepcopy(grid), 0  # Total distance accumlated for all buildings
    for i, row in enumerate(grid):
      for j, cell in enumerate(row):
        if cell != 1:
          continue
        min_dist, dist, dq = 1e9, [[0] * M for _ in range(N)], deque([(i, j)])
        while dq:
          r, c = dq.popleft()

          for nr, nc in next(r, c):
            dq.append((nr, nc))
            grid[nr][nc] -= 1
            dist[nr][nc] = dist[r][c] + 1
            total[nr][nc] += dist[nr][nc]

            min_dist = min(min_dist, total[nr][nc])

        target -= 1
    return min_dist if min_dist != 1e9 else -1
  ```
