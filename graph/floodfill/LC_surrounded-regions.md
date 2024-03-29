# [LC_surrounded-regions](https://leetcode.com/problems/surrounded-regions)

* en

  ```en
  Given an m x n matrix board containing 'X' and 'O', capture all regions surrounded by 'X'
  ```

* tc

  ```tc
  Input: board =
  [["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]]

  Output:
  [["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]]
  ```

## Solution

* py

  ```py
  def solve(self, G):
    n, m = len(G), len(G[0])
    boardFilter = lambda (i, j): 0 <= i < n and 0 <= j < m and G[i][j] == 'O'
    queue = filter(boardFilter, [x for i in range(max(n, m)) for x in ((i, 0), (i, m - 1), (0, i), (n - 1, i))])
    while queue:
      x, y = queue.pop()
      G[x][y] = 'M'
      queue.extend(filter(boardFilter, [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]))
    G[:] = [['XO'[x == 'M'] for x in row] for row in G]
  ```
