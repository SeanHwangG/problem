# [KT_beavergnaw](https://open.kattis.com/problems/beavergnaw)

* en

  ```en
  What should be the diameter 𝑑 of the inner cylinder such that the beaver chomped out V cubic units of wood?
  ```

* tc

  ```tc
  Input: 10 250
  20 2500
  25 7000
  50 50000
  0 0

  Output: 8.054498576
  14.774938880
  13.115314879
  30.901188723
  ```

## Solution

* py

  ```py
  import math
  while True:
    a, b = map(int, input().split())
    if a == b == 0:
      break
    print((a * a * a - 6 * b / math.pi) ** (1/3))
  ```
