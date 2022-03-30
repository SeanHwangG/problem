# [KT_timeloop](https://open.kattis.com/problems/timeloop)

Given N, Print 1 Abracadabra … N Abracadabra

```txt
Input: 2
Output:
1 Abracadabra
2 Abracadabra
```

## Solution

```py
n_line = int(input())
for i in range(1, n_line + 1):
  print(f"{i} Abracadabra")
```
