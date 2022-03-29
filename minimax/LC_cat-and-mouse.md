* Color each node marked DRAW, If any child is colored MOUSE, then this node will also be MOUSE
* Time. O(N ** 3)
* Space. O(N^2)

```py
def catMouseGame(self, G: List[List[int]]) -> int:
    N = len(G)
    def parents(m, c, t): # What nodes could play their turn to arrive at node (m, c, t)?
      if t == 2:
        for m2 in G[m]:
          yield m2, c, 3-t
      else:
        for c2 in G[c]:
          if c2:
            yield m, c2, 3-t

    DRAW, MOUSE, CAT = 0, 1, 2
    color = defaultdict(int)

    degree = {}  # degree[node] : the number of neutral children of this node
    for m in range(N):
      for c in range(N):
        degree[m, c, 1] = len(G[m])
        degree[m, c, 2] = len(G[c]) - (0 in G[c])

    dq = deque([])  # enqueued : all nodes that are colored
    for i in range(N):
      for t in range(1, 3):
        color[0, i, t] = MOUSE
        dq.append((0, i, t, MOUSE))
        if i > 0:
          color[i, i, t] = CAT
          dq.append((i, i, t, CAT))

    while dq:
      i, j, t, c = dq.popleft()
      for i2, j2, t2 in parents(i, j, t):
        if color[i2, j2, t2] is not DRAW:  # skip if this parent is colored
          continue
        # if the parent can make a winning move (ie. mouse to MOUSE), do so
        if t2 == c: # winning move
          color[i2, j2, t2] = c
          dq.append((i2, j2, t2, c))
          continue
        degree[i2, j2, t2] -= 1  # parent has degree[parent]--, enqueue if all children are colored as losing moves
        if degree[i2, j2, t2] == DRAW:
          color[i2, j2, t2] = 3 - t2
          dq.append((i2, j2, t2, 3 - t2))

    return color[1, 2, 1]
```
