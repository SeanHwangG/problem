```py
n = int(input())
ret = [1] * n
li = list(map(int, input().split()))
for i, n in enumerate(li):
  ret[n + 1] = i + 2
print(*ret)
```
