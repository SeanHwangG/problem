{% tabs %}{% tab title='LC_329.py' %}

```py
def longestIncreasingPath(self, G: List[List[int]]) -> int:
  @lru_cache(None)
  def dfs(x, y):
    length = 1
    for r, c in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
      if 0 <= r < len(G) and 0 <= c < len(G[0]) and G[x][y] < G[r][c]:
        length = max(length, dfs(r, c) + 1)
    return length
  if not any(G): return 0
  return max(dfs(i, j) for i in range(len(G)) for j in range(len(G[0])))
```

{% endtab %}{% endtabs %}