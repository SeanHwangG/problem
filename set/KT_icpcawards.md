```py
N = int(input())
seen = set()
for _ in range(N):
  uni, team = input().split()
  if uni not in seen and len(seen) < 12:
    print(uni, team)
  seen.add(uni)
```
