{% tabs %}{% tab title='LC_542.py' %}

```py
from collections import deque
class Solution:
  def updateMatrix(self, G):
    visited = set()
    q = deque()
    for i in range(len(G)):
      for j in range(len(G[0])):
        if G[i][j] == 0:
          visited.add((i,j))
          q.append((i,j))
    while q:
      r, c = q.popleft()
      for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if 0 <= nr < len(G) and 0 <= nc < len(G[0]) and (nr, nc) not in visited:
          G[nr][nc] = G[r][c] + 1
          visited.add((nr, nc))
          q.append((nr, nc))
    return G
```

{% endtab %}{% endtabs %}