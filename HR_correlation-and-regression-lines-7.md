```py
import math
x, y = list(map(int, input().split())), list(map(int, input().split()))
x = [a - sum(x) / len(x) for a in x]
y = [a - sum(y) / len(y) for a in y]
slope = sum([a * b for a, b in zip(x, y)]) / sum([a * a for a in x])
print(f"{slope:.3f}")
```
