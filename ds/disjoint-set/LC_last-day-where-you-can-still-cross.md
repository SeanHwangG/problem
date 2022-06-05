# [LC_last-day-where-you-can-still-cross](https://leetcode.com/problems/last-day-where-you-can-still-cross)

```en
Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water
Find last possible day that to walk from the top to the bottom by only walking on land cells (left, right, up, down)
You can start from any cell in the top row and end at any cell in the bottom row
```

```txt
Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
Output: 2

Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
Output: 1
```

## Solution

* Time; O(n * log n)

* py

  ```py
  def latestDayToCross(self, row: int, col: int, A: List[List[int]]) -> int:
    def find(x):
      parents.setdefault(x, x)
      if x != parents[x]:
        parents[x] = find(parents[x])
      return parents[x]
    def union(x, y):
      parents[find(x)] = find(y)
    vis, top, parents = set(), set(), {}
    for r in range(1, row + 1):
      union('l', (r, 1))
      union('r', (r, col))
    for i, (r, c) in enumerate(A):
      vis.add((r, c))
      for nr, nc in [(r + dr, c + dc) for dr in [1, 0, -1] for dc in [1, 0, -1]]:
        if (nr, nc) in vis:
          union((r, c), (nr, nc))
      if find('l') == find('r'):
        return i
  ```
