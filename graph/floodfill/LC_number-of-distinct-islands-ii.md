# [LC_number-of-distinct-islands-ii](https://leetcode.com/problems/number-of-distinct-islands-ii)

* en

  ```en
  Island is group of 1's (representing land) connected 4-directionally (horizontal or vertical)
  Island is considered to be the same as another if they have same shape, or have same shape after rotation or reflection
  ```

* tc

  ```tc
  Input:
  grid =
  [[1,1,0,0,0],
   [1,0,0,0,0],
   [0,0,0,0,1],
   [0,0,0,1,1]]

  Output: 1
  ```

## Solution

* py

  ```py
  def dfs(self, G, r, c, shape):
    G[r][c] = 0
    shape.append((r, c))
    for nr, nc in [(r, c - 1), (r - 1, c), (r, c + 1), (r + 1, c)]:
      if 0 <= nr < len(G) and 0 <= nc < len(G[0]) and G[nr][nc] != 0:
        self.dfs(G, nr, nc, shape)

  def normalize(self, shape):
    rotated_shapes, norm_res = [[] for _ in range(8)], []

    for x, y in shape:
      rotated_shapes[0].append((x, y))
      rotated_shapes[1].append((-x, y))
      rotated_shapes[2].append((x, -y))
      rotated_shapes[3].append((-x, -y))
      rotated_shapes[4].append((y, x))
      rotated_shapes[5].append((-y, x))
      rotated_shapes[6].append((y, -x))
      rotated_shapes[7].append((-y, -x))

    for rs in rotated_shapes:
      rs.sort()
      tmp = [(0, 0)]
      for i in range(1, len(rs)):
        tmp.append((rs[i][0] - rs[0][0], rs[i][1] - rs[0][1]))
      norm_res.append(tmp[:])
    norm_res.sort()

    return tuple(norm_res[0])

  def numDistinctIslands2(self, G: list[list[int]]) -> int:
    res = set()
    for r in range(0, len(G)):
      for c in range(0, len(G[0])):
        if G[r][c] == 1:
          shape = []
          self.dfs(G, r, c, shape)
          norm = self.normalize(shape)
          res.add(norm)

    return len(res)
  ```
