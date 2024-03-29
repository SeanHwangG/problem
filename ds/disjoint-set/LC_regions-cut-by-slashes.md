# [LC_regions-cut-by-slashes](https://leetcode.com/problems/regions-cut-by-slashes)

* en

  ```en
  In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space
  These characters divide the square into contiguous regions
  Return the number of regions
  ```

* tc

  ```tc
  Input:
  [ " /",
    "/ " ]
  Output: 2
  ```

## Solution

* py

  ```py
  def regionsBySlashes(self, grid: List[str]) -> int:
    f = {}
    def find(x):
      f.setdefault(x, x)
      if x != f[x]:
        f[x] = find(f[x])
      return f[x]
    def union(x, y):
      f[find(x)] = find(y)

    for i in range(len(grid)):
      for j in range(len(grid)):
        if i:
          union((i - 1, j, 2), (i, j, 0))
        if j:
          union((i, j - 1, 1), (i, j, 3))
        if grid[i][j] != "/":
          union((i, j, 0), (i, j, 1))
          union((i, j, 2), (i, j, 3))
        if grid[i][j] != "\\":
          union((i, j, 3), (i, j, 0))
          union((i, j, 1), (i, j, 2))
    return len(set(map(find, f)))
  ```
