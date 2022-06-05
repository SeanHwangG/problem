# [LC_is-graph-bipartite](https://leetcode.com/problems/is-graph-bipartite)

```en
Graph is bipartite if the nodes can be partitioned into two independent sets A and B
S.T. every edge in the graph connects a node in set A and a node in set B
Return if given graph is bipartite
```

```txt
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false

Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
```

## Solution

* py

  ```py
  def isBipartite(self, G):
    color = {}
    def dfs(pos):
      for i in G[pos]:
        if i in color:
          if color[i] == color[pos]:
            return False
        else:
          color[i] = 1 - color[pos]
          if not dfs(i):
            return False
      return True
    for i in range(len(G)):
      if i not in color:
        color[i] = 0
        if not dfs(i):
          return False
    return True
  ```
