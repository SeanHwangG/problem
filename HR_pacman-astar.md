{% tabs %}{% tab title='HR_pacman-astar.py' %}

```py
from collections import deque

start_r, start_c = map(int, input().split())
food_r, food_c = map(int, input().split())
n, m = map(int, input().split())
G = [list(map(str, input())) for i in range(0, n)]
dq = deque()
answer_routes = None

dq.append([start_r, start_c, [], 0])
while len(dq) > 0:
  r, c, last_route, score = dq.popleft()
  routes = last_route.copy()
  routes.append([r, c])

  if (r, c) == (food_r, food_c) and not answer_routes:
    answer_routes = routes
    break

  moves = []
  for next_x, next_y in ([r - 1, c], [r, c - 1], [r, c + 1], [r + 1, c]):
    if next_x < 0 or next_x >= n or next_y < 0 and next_y >= n:
      continue

    if G[next_x][next_y] == "-" or G[next_x][next_y] == ".":
      G[next_x][next_y] = '='
      moves.append([next_x, next_y, score + abs(food_r - next_x) + abs(food_c - next_y)])

  moves.sort(key = lambda move: move[2])
  for move in moves:
    dq.append([move[0], move[1], routes, score])

print(str(len(answer_routes) - 1))
for point in answer_routes:
  print(f"{point[0]} {point[1]}")
```

{% endtab %}{% endtabs %}
