```py
n_test = int(input())
for i in range(n_test):
  N = int(input())
  li = list(map(int, input().split()))
  print((max(li) - min(li)) * 2)
```
