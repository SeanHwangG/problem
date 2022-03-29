```py
def minimumEffort(self, tasks: List[List[int]]) -> int:
  sort = sorted(tasks, key = lambda x : x[1] - x[0])[::-1]
  res = 0; curr = 0
  for i, n in enumerate(sort):
    if curr < n[1]:
      res += n[1] - curr
      curr = n[1]
    curr -= n[0]
  return res
```
