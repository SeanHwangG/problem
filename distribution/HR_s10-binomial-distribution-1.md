```py
from math import comb

def binomial(x, n, p):
  return comb(n, x) * p ** x * (1 - p) ** (n - x)

l, r = map(float, input().split())
odds = l / r
print(round(sum([binomial(i, 6, odds / (1 + odds)) for i in range(3, 7)]), 3))
```