# [KT_ladder](https://open.kattis.com/problems/ladder)



```txt
Input: 500 70
Output: 533
```

## Solution

* py

  ```py
  import math
  a, theta = map(int, input().split())
  print(math.ceil(a / math.sin(theta / 180 * math.pi)))
  ```
