```py
import statistics as stats

N = int(input())
X = list(map(int, input().split()))

print(f"{stats.pstdev(X):.1f}")
```
