```py
n_match, w, h = map(int, input().split())
mx = (w ** 2 + h ** 2) ** 0.5
for _ in range(n_match):
  x = int(input())
  if x <= mx:
    print('DA')
  else:
    print('NE')
```
