# [KT_railroad2](https://open.kattis.com/problems/railroad2)



```txt
Input: 0 2
Output: possible
```

## Solution

* py

  ```py
  a, b = map(int, input().split())
  print("possible" if b % 2 == 0 else "impossible")
  ```
