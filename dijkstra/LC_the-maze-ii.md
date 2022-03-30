# [LC_the-maze-ii](https://leetcode.com/problems/the-maze-ii)

Given ball in maze with empty spaces (0) and walls (1), which can go through empty spaces by up, down, left or right
But it won't stop rolling until hitting a wall, and when the ball stops, it could choose the next direction
Return shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1

```txt
Input: maze =
[[0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [1,1,0,1,1],
 [0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: 12
```

## Solution

```py
def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
  m, n, q, stopped = len(maze), len(maze[0]), [(0, start[0], start[1])], {(start[0], start[1]): 0}
  while q:
    dist, x, y = heapq.heappop(q)
    if [x, y] == destination:
      return dist
    for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
      newX, newY, d = x, y, 0
      while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
        newX += i
        newY += j
        d += 1
      if (newX, newY) not in stopped or dist + d < stopped[(newX, newY)]:
        stopped[(newX, newY)] = dist + d
        heapq.heappush(q, (dist + d, newX, newY))
  return -1
```
