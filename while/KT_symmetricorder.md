```py
si = 0
while n := int(input()) != 0:
  si += 1
  print(f"SET {si}")
  li = [input() for _ in range(n)]
  for i in range(0, n, 2):
    print(li[i])
  for i in range(1, n, 2):
    print(li[i])
```
