```py
def hasPath(self, G: List[List[int]], start: List[int], goal: List[int]) -> bool:
  Q = deque([start])
  dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

  while Q:
    i, j = Q.popleft()
    G[i][j] = 2

    if i == goal[0] and j == goal[1]:
      return True

    for x, y in dirs:
      row, col = i + x, j + y
      while 0 <= row < len(G) and 0 <= col < len(G[0]) and G[row][col] != 1:
        row, col = row + x, col + y
      row -= x
      col -= y
      if G[row][col] == 0:
        Q.append([row, col])

  return False
```
