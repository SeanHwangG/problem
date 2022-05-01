# [KT_cudoviste](https://open.kattis.com/problems/cudoviste)



```txt
Input:
4 4
#..#
..X.
..X.
#XX#

Output:
1
1
2
1
0
```

## Solution

* py

  ```py
  N, M = map(int, input().split())
  G = []
  for _ in range(N):
    G.append(input())
  rets = [0, 0, 0, 0, 0]
  for i in range(1, N):
    for j in range(1, M):
      spaces = [G[i - 1][j - 1], G[i - 1][j], G[i][j - 1], G[i][j]]
      if '#' in spaces:
        continue
      rets[spaces.count('X')] += 1
  for ret in rets:
    print(ret)
  ```
