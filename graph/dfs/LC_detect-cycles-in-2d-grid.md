# [LC_detect-cycles-in-2d-grid](https://leetcode.com/problems/detect-cycles-in-2d-grid)

```en
Given a 2D array of grid of size m x n, find if there exists any cycle consisting of the same value in grid
```

```txt
Input: grid =
[["a","a","a","a"],
 ["a","b","b","a"],
 ["a","b","b","a"],
 ["a","a","a","a"]]
Output: true
```

## Solution

* py

  ```py
  def containsCycle(self, G: List[List[str]]) -> bool:
    seen = defaultdict(int)
    def dfs(r, c, p):
      if seen[r, c]: return seen[r,c] == -1
      seen[r, c] = -1
      for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
        if (nr, nc) == p: continue
        if len(G) > nr >= 0 <= nc < len(G[0]) and G[nr][nc] == G[r][c] and dfs(nr, nc, (r, c)):
          return True
      seen[r, c] = 1
      return False
    return any(not seen[r, c] and dfs(r, c, -1) for r, c in product(range(len(G)), range(len(G[0]))))
  ```
