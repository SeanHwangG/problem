# [KT_autori](https://open.kattis.com/problems/autori)



```txt
Input: Knuth-Morris-Pratt
Output: KMP
```

## Solution

* py

  ```py
  st = input()
  for i, ch in enumerate(st):
    if i == 0 or st[i - 1] == '-':
      print(st[i], end='')
  ```
