# [KT_timeloop](https://open.kattis.com/problems/timeloop)

* en

  ```en
  Given N, Print 1 Abracadabra … N Abracadabra
  ```

* tc

  ```tc
  Input: 2
  Output:
  1 Abracadabra
  2 Abracadabra
  ```

## Solution

* py

  ```py
  n_line = int(input())
  for i in range(1, n_line + 1):
    print(f"{i} Abracadabra")
  ```
