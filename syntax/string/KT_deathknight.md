# [KT_deathknight](https://open.kattis.com/problems/deathknight)

Given N lines, count number of lines without CD

```txt
Input: 3
DCOOO
DODOCD
COD

Output: 2
```

## Solution

* py

  ```py
  n = int(input())
  ret = 0
  for _ in range(n):
    if 'CD' not in input():
      ret += 1
  print(ret)
  ```
