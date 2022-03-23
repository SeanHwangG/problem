```py
w = int(input())
total = 0
for _ in range(int(input())):
  a, b = map(int, input().split())
  total += a * b
print(total // w)
```
