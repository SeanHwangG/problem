```py
def nextClosestTime(self, time: str) -> str:
  return min((t <= time, t)
              for i in range(24 * 60)
              for t in ['%02d:%02d' % divmod(i, 60)] if set(t) <= set(time))[1]
```
