# [KT_differentdistances](https://open.kattis.com/problems/differentdistances)



```txt
Input: 1.0 1.0 2.0 2.0 2.0
1.0 1.0 2.0 2.0 1.0
1.0 1.0 20.0 20.0 10.0
0
Output:
1.4142135624
2.0000000000
20.3636957882
```

## Solution

* py

```py
while True:
  raw = input()
  if raw == '0':
    break
  a, b, c, d, e = map(float, raw.split())
  print((abs(a - c) ** e + abs(b - d) ** e) ** (1/e))
```
