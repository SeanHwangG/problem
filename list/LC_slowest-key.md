```py
def slowestKey(self, r, k):
  return max(zip(map(sub, r, [0, *r]), k))[1]
```
