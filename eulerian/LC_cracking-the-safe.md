```py
def crackSafe(self, n: int, k: int) -> str:
  visited = set()
  res = s = '0' * (n - 1)
  while True:
    for i in range(k - 1, -1, -1):
      if (s, i) not in visited:
        res += str(i)
        visited.add((s, i))
        s = (s + str(i))[1:]
        break
    else:
      return res
```
