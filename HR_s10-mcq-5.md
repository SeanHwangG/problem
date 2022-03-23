```py
from fractions import Fraction
from itertools import combinations
cards = [(t, n) for t in "HDCS" for n in range(1, 14)]
combs, s = list(combinations(cards, 2)), 0
for a, b in combs:
  if a[0] == b[0]:
    s += 1
print(Fraction(s, len(combs)))
```
