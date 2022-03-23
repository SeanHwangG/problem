```py
mn = int(input())
mx = int(input())
sm = int(input())
def match(n, sm):
  while n != 0:
    sm -= n % 10
    n //= 10
  return sm == 0
for i in range(mn, mx + 1):
  if match(i, sm):
    print(i)
    break
for i in range(mx, mn - 1, -1):
  if match(i, sm):
    print(i)
    break
```
