# [KT_pot](https://open.kattis.com/problems/pot)

* en

  ```en
  Print number when last number is exponent
  ```

* tc

  ```tc
  Input: 5
  23
  17
  43
  52
  22

  Output: 102  # 2 ** 3 + 1 ** 7 ..
  ```

## Solution

* py

  ```py
  n_line = int(input())
  ret = 0
  for _ in range(n_line):
    n = int(input())
    ret += (n // 10) ** (n % 10)
  print(ret)
  ```
