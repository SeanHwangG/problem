# [KT_tarifa](https://open.kattis.com/problems/tarifa)



```txt
Input:
10
3
4
6
2

Output: 28
```

## Solution

* py

  ```py
  add = int(input())
  n_line = int(input())
  cur = 0
  for n in range(n_line):
    cur += add
    cur = max(0, cur - int(input()))
  print(cur + add)
  ```
