# [LC_cat-and-mouse](https://leetcode.com/problems/cat-and-mouse)

* en

  ```en
  Game on an undirected graph is played by two players, Mouse and Cat, who alternate turns
  Graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of graph
  Mouse starts at node 1 and goes first, the cat starts at node 2 and goes second, and hole is at node 0
  During each player's turn, they must travel along one edge of the graph that meets where they are
  For example, if the Mouse is at node 1, it must travel to any node in graph[1]
  Then, the game can end in three ways:
    If ever the Cat occupies the same node as the Mouse, the Cat wins
    If ever the Mouse reaches the Hole, Mouse wins (cat cannot travel to Hole)
    If ever position is repeated (ex: players in same position as previous, and it is same player's turn to move), draw
  Given a graph, and assuming both players play optimally, return 1 if the mouse wins, 2 if the cat wins, or 0 if draw
  ```

* tc

  ```tc
  Input: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
  Output: 0

  Input: graph = [[1,3],[0],[3],[0,2]]
  Output: 1
  ```

## Solution

* Color each node marked DRAW, If any child is colored MOUSE, then this node will also be MOUSE
* Time. O(N ** 3)
* Space. O(N^2)

* py

  ```py
  def catMouseGame(self, G: List[List[int]]) -> int:
      N = len(G)
      def parents(m, c, t): # What nodes could play their turn to arrive at node (m, c, t)?
        if t == 2:
          for m2 in G[m]:
            yield m2, c, 3-t
        else:
          for c2 in G[c]:
            if c2:
              yield m, c2, 3-t

      DRAW, MOUSE, CAT = 0, 1, 2
      color = defaultdict(int)

      degree = {}  # degree[node] : the number of neutral children of this node
      for m in range(N):
        for c in range(N):
          degree[m, c, 1] = len(G[m])
          degree[m, c, 2] = len(G[c]) - (0 in G[c])

      dq = deque([])  # enqueued : all nodes that are colored
      for i in range(N):
        for t in range(1, 3):
          color[0, i, t] = MOUSE
          dq.append((0, i, t, MOUSE))
          if i > 0:
            color[i, i, t] = CAT
            dq.append((i, i, t, CAT))

      while dq:
        i, j, t, c = dq.popleft()
        for i2, j2, t2 in parents(i, j, t):
          if color[i2, j2, t2] is not DRAW:  # skip if this parent is colored
            continue
          # if the parent can make a winning move (ie. mouse to MOUSE), do so
          if t2 == c: # winning move
            color[i2, j2, t2] = c
            dq.append((i2, j2, t2, c))
            continue
          degree[i2, j2, t2] -= 1  # parent has degree[parent]--, enqueue if all children are colored as losing moves
          if degree[i2, j2, t2] == DRAW:
            color[i2, j2, t2] = 3 - t2
            dq.append((i2, j2, t2, 3 - t2))

      return color[1, 2, 1]
  ```
