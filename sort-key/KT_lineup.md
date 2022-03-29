```py
n = int(input())
li = []
for _ in range(n):
  li.append(input())
if li == sorted(li):
  print("INCREASING")
elif li == sorted(li, reverse=True):
  print('DECREASING')
else:
  print('NEITHER')
```
