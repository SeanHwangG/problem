```py
n = int(input())
ret = 0
for _ in range(n):
  if 'CD' not in input():
    ret += 1
print(ret)
```