```py
N = int(input())
for _ in range(N):
  st1 = input()
  st2 = input()
  print(st1)
  print(st2)
  for c1, c2 in zip(st1, st2):
    if c1 == c2:
      print('.', end='')
    else:
      print('*', end='')
  print()
```
