```py
def canConstruct(self, s, k):
  return sum(i & 1 for i in collections.Counter(s).values()) <= k <= len(s)
```