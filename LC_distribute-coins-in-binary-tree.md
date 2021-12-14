{% tabs %}{% tab title='LC_979.py' %}

```py
res = 0
def distributeCoins(self, root):
  def dfs(root):
    if not root: return 0
    left = dfs(root.left)
    right = dfs(root.right)
    self.res += abs(left) + abs(right)
    return root.val + left + right - 1
  dfs(root)
  return self.res
```

{% endtab %}{% endtabs %}
