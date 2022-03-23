```py
frac = list(map(int, input().split()))
p = frac[0] / frac[1]
n = int(input())
q = 1 - p
print(round(1 - q ** n,3))
```
