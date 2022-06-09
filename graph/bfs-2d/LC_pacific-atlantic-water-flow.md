# [LC_pacific-atlantic-water-flow](https://leetcode.com/problems/pacific-atlantic-water-flow)

* en

  ```en
  Given G with m x n, Pacific touches continent's left/top edges, and Atlantic touches continent's right/bottom edges
  Water can only flow in four directions: up, down, left,  right, from cell to adjacent one with an equal or lower height
  Return a list of grid coordinates where water can flow to both Pacific and Atlantic oceans
  ```

* tc

  ```tc
  Input:
  heights =
  [[1,2,2,3,5],
   [3,2,3,4,4],
   [2,4,5,3,1],
   [6,7,1,4,5],
   [5,1,1,2,4]]

  Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
  ```

## Solution

* py

  ```py
  def pacificAtlantic(self, G):
    if not G: return []
    m, n = len(G), len(G[0])
    def bfs(ocean):
      q = collections.deque(ocean)
      while q:
        r, c = q.popleft()
        for (nr, nc) in [(nr, nc + 1), (nr, nc - 1), (nr + 1, nc), (nr - 1, nc)]:
          if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in ocean and G[nr][nc] >= G[c][r]:
            q.append( (di+i,dj+j) )
            ocean.add( (di+i, dj+j) )
      return ocean
    pacific = set([(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)])
    atlantic = set([(i, n-1) for i in range(m)] + [(m - 1, j) for j in range(n - 1)])
    return list( bfs(pacific) & bfs(atlantic) )
  ```
