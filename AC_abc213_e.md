{% tabs %}{% tab title='AC_abc213_e.py' %}

```py
from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

q = deque([(0, 0, 0)])
dp = [[10**9 for _ in range(W)] for _ in range(H)]
while q:
  n, r, c = q.popleft()
  for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
    if nr < 0 or nc < 0 or nr >= H or nc >= W:
      continue
    if S[nr][nc] == "." and dp[nr][nc] > n:
      dp[nr][nc] = n
      q.appendleft([n, nr, nc])
  for dx in [-2, -1, 0, 1, 2]:
    for dy in [-2, -1, 0, 1, 2]:
      if abs(dx) + abs(dy) == 4:
        continue
      if r + dx < 0 or c + dy < 0 or r + dx >= H or c + dy >= W:
        continue
      if dp[r + dx][c + dy] > c + 1:
        dp[r + dx][c + dy] = c + 1
        q.append([c + 1, r + dx, c + dy])
print(dp[-1][-1])
```

{% endtab %}{% endtabs %}
