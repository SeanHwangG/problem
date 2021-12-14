{% tabs %}{% tab title='LC_337.py' %}

```py
def rob(self, root: TreeNode):
  def with_without_rob(root):
    if root :
      wi_l, wo_l = with_without_rob(root.left)
      wi_r, wo_r = with_without_rob(root.right)
      return (root.val + wo_l + wo_r, max(wi_l, wo_l) + max(wi_r, wo_r))
    return (0, 0)

  return max(with_without_rob(root))
```

{% endtab %}{% endtabs %}
