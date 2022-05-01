# [LC_shortest-path-to-get-all-keys](https://leetcode.com/problems/shortest-path-to-get-all-keys)

Given an m x n grid grid where:
  '.' is an empty cell
  '#' is a wall
  '@' is starting point
  Lowercase letters represent keys
  Uppercase letters represent locks
Return lowest number of moves to acquire all keys. If it is impossible, return -1

```txt
Input: grid =
["@.a.#",
 "###.#",
 "b.A.B"]
Output: 8

Input: grid =
["@..aA",
 "..B#.",
 "....b"]
Output: 6
```

## Solution

* Time; O(MN key)

* py

  ```py
  def shortestPathAllKeys(self, G: List[str]) -> int:
    final, N, M, si, sj = 0, len(G), len(G[0]), 0, 0
    for i in range(N):
      for j in range(M):
        if G[i][j] in "abcdef":
          final |= 1 << ord(G[i][j]) - ord("a")
        if G[i][j] == "@":
          si, sj = i, j
    q, memo = deque([(0, si, sj, 0)]), set()
    while q:
      moves, i, j, state = q.popleft()
      if state == final:
        return moves
      for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if N > x >= 0 <= y < M and G[x][y] != "#":
          if G[x][y].isupper() and not state & 1 << (ord(G[x][y].lower()) - ord("a")): continue
          newState = ord(G[x][y]) >= ord("a") and state | 1 << (ord(G[x][y]) - ord("a")) or state
          if (newState, x, y) not in memo:
            memo.add((newState, x, y))
            q.append((moves + 1, x, y, newState))
    return -1
  ```
