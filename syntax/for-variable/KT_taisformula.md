# [KT_taisformula](https://open.kattis.com/problems/taisformula)

```en
Each N line contains, where ti is the time of the sample, and vi is the glucose value at time ti
```

```txt
Input: 3  # N
1000 2.0   # ti, vi
2000 12.0
3000 22.0

Output: 24
```

## Solution

* py

  ```py
  pa, pb = None, None
  ret = 0
  for _ in range(int(input())):
    a, b = map(float, input().split())
    if pa != None:
      ret += (a - pa) * (b + pb) / 2 / 1000
    pa, pb = a, b
  print(ret)
  ```
