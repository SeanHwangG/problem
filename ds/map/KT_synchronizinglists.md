# [KT_synchronizinglists](https://open.kattis.com/problems/synchronizinglists)

* en

  ```en
  For each line, print second list so that it has same ordering as first list, with blank line between lists
  ```

* tc

  ```tc
  Input:
  4
  10
  67
  68
  28
  55
  73
  10
  6
  7
  98
  23
  61
  49
  1
  79
  9
  1
  15
  32
  47
  68
  39
  24
  0

  Output:
  6
  55
  73
  10

  68
  24
  39
  32
  1
  47
  15
  ```

## Solution

* py

  ```py
  while True:
    n = int(input())

    if n == 0:
      break

    l1 = [int(input()) for _ in range(n)]
    l2 = list(sorted([int(input()) for _ in range(n)]))
    rank = {}
    for i, e in enumerate(sorted(l1)):
      rank[e] = i
    for e in l1:
      print(l2[rank[e]])
    print()
  ```
