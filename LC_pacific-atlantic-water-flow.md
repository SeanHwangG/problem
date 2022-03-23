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
