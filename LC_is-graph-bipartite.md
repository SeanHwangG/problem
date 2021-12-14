{% tabs %}{% tab title='LC_785.py' %}

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

{% endtab %}{% endtabs %}
