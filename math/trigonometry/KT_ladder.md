# [KT_ladder](https://open.kattis.com/problems/ladder)

```en

```

```kr
높이 h와 각도 theta가 주어질 때 사다리의 최소 길이를 구하여라. (ceil)
```

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
