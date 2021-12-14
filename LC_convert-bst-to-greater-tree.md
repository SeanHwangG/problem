{% tabs %}{% tab title='LC_538.py' %}

```py
class Solution:
  def __init__(self):
    self.total = 0

  def convertBST(self, root: TreeNode) -> TreeNode:
    if not root:
      return
    self.convertBST(root.right)
    root.val += self.total
    self.total = root.val
    self.convertBST(root.left)
    return root
```

{% endtab %}{% endtabs %}
