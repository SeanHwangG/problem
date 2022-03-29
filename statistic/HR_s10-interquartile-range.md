```py
import statistics as st
n = int(input())
X = list(map(int, input().split()))
F = list(map(int, input().split()))

S = list(sorted(X[i] for i in range(n) for _ in range(F[i])))

n = len(S)
n2 = int(n/2)
print(round(float(st.median(S[-n2:])-st.median(S[:n2])),1))
```
