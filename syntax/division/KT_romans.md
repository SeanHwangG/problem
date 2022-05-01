# [KT_romans](https://open.kattis.com/problems/romans)

One mile is 1000 * 5280 / 4854 pace, Print pace when given miles (decimal point is rounded off)

```txt
Input: 20.267
Output: 22046
```

## Solution

* py

  ```py
  n = float(input())
  print(int(n * 5280000 / 4854 + 0.5))
  ```
