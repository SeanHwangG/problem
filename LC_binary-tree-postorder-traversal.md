{% tabs %}{% tab title='LC_145.py' %}

```py
def postorderTraversal(self, root):
  traversal, stack = [], [root]
  while stack:
    node = stack.pop()
    if node:
      traversal.append(node.val)
      stack.extend([node.left, node.right])
  return traversal[::-1]
```

{% endtab %}{% endtabs %}
