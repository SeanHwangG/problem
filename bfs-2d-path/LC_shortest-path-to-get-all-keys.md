* Time; O(MN key)

```py
def shortestPathAllKeys(self, G: List[str]) -> int:
  final, N, M, si, sj = 0, len(G), len(G[0]), 0, 0
  for i in range(N):
    for j in range(M):
      if G[i][j] in "abcdef":
        final |= 1 << ord(G[i][j]) - ord("a")
      if G[i][j] == "@":
        si, sj = i, j
  q, memo = deque([(0, si, sj, 0)]), set()
  while q:
    moves, i, j, state = q.popleft()
    if state == final:
      return moves
    for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
      if N > x >= 0 <= y < M and G[x][y] != "#":
        if G[x][y].isupper() and not state & 1 << (ord(G[x][y].lower()) - ord("a")): continue
        newState = ord(G[x][y]) >= ord("a") and state | 1 << (ord(G[x][y]) - ord("a")) or state
        if (newState, x, y) not in memo:
          memo.add((newState, x, y))
          q.append((moves + 1, x, y, newState))
  return -1
```
