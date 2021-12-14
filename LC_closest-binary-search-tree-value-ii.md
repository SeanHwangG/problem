{% tabs %}{% tab title='LC_272.py' %}

```py
def closestKValues(self, root, target, k):
  def vals(root):
    return vals(root.left) + [root.val] + vals(root.right) if root else []
  return sorted(vals(root), key=lambda x: abs(x - target))[:k]
```

{% endtab %}{% endtabs %}
