# [LC_the-maze](https://leetcode.com/problems/the-maze)

* en

  ```en
  Through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting wall
  When the ball stops, it could choose the next direction.
  Given m x n maze, ball's start position and destination, return if ball can stop at destination
  ```

* tc

  ```tc
  Input: maze =
    [[0,0,1,0,0],
     [0,0,0,0,0],
     [0,0,0,1,0],
     [1,1,0,1,1],
     [0,0,0,0,0]], start = [0,4], destination = [4,4]
  Output: true  # left -> down -> left -> down -> right -> down -> right.
  ```

## Solution

* py

  ```py
  def hasPath(self, G: List[List[int]], start: List[int], goal: List[int]) -> bool:
    Q = deque([start])
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

    while Q:
      i, j = Q.popleft()
      G[i][j] = 2

      if i == goal[0] and j == goal[1]:
        return True

      for x, y in dirs:
        row, col = i + x, j + y
        while 0 <= row < len(G) and 0 <= col < len(G[0]) and G[row][col] != 1:
          row, col = row + x, col + y
        row -= x
        col -= y
        if G[row][col] == 0:
          Q.append([row, col])

    return False
  ```
