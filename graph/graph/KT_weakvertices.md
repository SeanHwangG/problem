# [KT_weakvertices](https://open.kattis.com/problems/weakvertices)

* en

  ```en
  Weak vertices in graphs – those vertices that is not part of any triangle
  ```

* tc

  ```tc
  Input:
  9
  0 1 1 1 0 0 0 0 0
  1 0 0 0 0 0 1 0 0
  1 0 0 1 0 1 0 0 0
  1 0 1 0 0 1 1 0 0
  0 0 0 0 0 0 1 1 0
  0 0 1 1 0 0 0 0 0
  0 1 0 1 1 0 0 1 0
  0 0 0 0 1 0 1 0 1
  0 0 0 0 0 0 0 1 0
  1
  0
  -1

  Output:
  1 8
  0
  ```

## Solution

* py

  ```py
  from collections import defaultdict
  while True:
    N = int(input())
    if N == -1:
      break
    G = defaultdict(set)
    for i in range(N):
      for j, e in enumerate(list(map(int, input().split()))):
        if e == 1:
          G[i].add(j)
    for i in range(N):
      count = 0
      for j in G[i]:
        count += sum([1 for k in G[j] if k in G[i]])
      if count == 0:
        print(i, end = ' ')
    print()
  ```
