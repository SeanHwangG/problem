{% tabs %}{% tab title='LC_236.py' %}

* Time / space; O(n) / O(n)

```py
def lowestCommonAncestor(self, root, p, q):
  if root in (None, p, q): return root
  left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
  return root if left and right else left or right
```

{% endtab %}{% endtabs %}
