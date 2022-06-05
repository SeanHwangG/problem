# [LC_the-maze-iii](https://leetcode.com/problems/the-maze-iii)

```en
Ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting wall
Return string instructions of all instructions that ball should follow to drop in hole with shortest distance possible
Print lexicographically minimum in case of tie
```

```txt
Input: maze =
[[0,0,0,0,0],
 [1,1,0,0,1],
 [0,0,0,0,0],
 [0,1,0,0,1],
 [0,1,0,0,0]], ball = [4,3], hole = [0,1]
Output: "lul"

Input: maze =
[[0,0,0,0,0],
 [1,1,0,0,1],
 [0,0,0,0,0],
 [0,1,0,0,1],
 [0,1,0,0,0]], ball = [4,3], hole = [3,0]
Output: "impossible"
```

## Solution

* py

  ```py
  def findShortestWay(self, G, ball, hole):
    ball, hole = tuple(ball), tuple(hole)
    def neighbors(r, c):
      for dr, dc, di in [(-1, 0, 'u'), (0, 1, 'r'), (0, -1, 'l'), (1, 0, 'd')]:
        cr, cc, dist = r, c, 0
        while 0 <= cr + dr < len(G) and  0 <= cc + dc < len(G[0]) and not G[cr+dr][cc+dc]:
          cr += dr
          cc += dc
          dist += 1
          if (cr, cc) == hole:
            break
        yield (cr, cc), di, dist

    pq, seen = [(0, '', ball)], set()
    while pq:
      dist, path, node = heapq.heappop(pq)
      if node in seen: continue
      if node == hole: return path
      seen.add(node)
      for nei, di, nei_dist in neighbors(*node):
        heapq.heappush(pq, (dist+nei_dist, path+di, nei))

    return "impossible"
  ```
