```py
from fractions import Fraction
poss = ["BG", "BB", "GB", "GG"]
print(f"Probability: {Fraction(sum(p == 'BB' for p in poss), sum('B' in p for p in poss))}")
```
