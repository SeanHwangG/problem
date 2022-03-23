```py
from math import comb

def b(x, n, p):
  return comb(n, x) * p**x * (1-p)**(n-x)

p, n = map(int, input().split())
print(round(sum([b(i, n, p / 100) for i in range(3)]), 3))
print(round(sum([b(i, n, p / 100) for i in range(2, n+1)]), 3))
```
