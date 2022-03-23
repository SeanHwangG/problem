```py
n_test = int(input())
for i in range(n_test):
  t, n = map(int, input().split())
  print(t, n + (n * (n + 1)) // 2)
```
