# [LC_swim-in-rising-water](https://leetcode.com/problems/swim-in-rising-water)

Given an n x n integer matrix grid where each value grid[i][j] represents elevation at that point (i, j)
Rain starts to fall. At time t, depth of water everywhere is t
Can swim from square to another 4-directionally adjacent iff elevation of both squares individually are at most t
Can swim infinite distances in zero time. Of course, you must stay within boundaries of grid during your swim
Return least time until you can reach bottom right square (n - 1, n - 1) if start at top left square (0, 0)

```txt
Input: grid = [[0,2],[1,3]]
Output: 3

Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
```

## Solution

```py
def swimInWater(self, grid: List[List[int]]) -> int:
  N, pq, seen, res = len(grid), [(grid[0][0], 0, 0)], set([(0, 0)]), 0
  while True:
    T, x, y = heapq.heappop(pq)
    res = max(res, T)
    if x == y == N - 1:
      return res
    for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
      if 0 <= i < N and 0 <= j < N and (i, j) not in seen:
        seen.add((i, j))
        heapq.heappush(pq, (grid[i][j], i, j))
```
