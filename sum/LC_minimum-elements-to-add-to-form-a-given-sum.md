```py
def minElements(self, A, limit, goal):
  return (abs(sum(A) - goal) + limit - 1) / limit
```