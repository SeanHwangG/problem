# [KT_herman](https://open.kattis.com/problems/herman)

```en
Print area of circle with radius n. then print n ** 2 * 2
```

```txt
Input: 1
Output:
3.141593
2.000000
```

## Solution

* py

  ```py
  import math
  n = int(input())
  print(n * n * math.pi)
  print(n * n * 2)
  ```
