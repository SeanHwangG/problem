{% tabs %}{% tab title='LC_101.go' %}

```go
func isSymmetric(root *TreeNode) bool {
  return helper(root, root)
}

func helper(left *TreeNode, right *TreeNode) bool {
  if left == nil && right == nil {
    return true
  }
  if left == nil || right == nil {
    return false
  }
  return left.Val == right.Val && helper(left.Right, right.Left) && helper(left.Left, right.Right)
}
```

{% endtab %}{% tab title='LC_101.py' %}

```py
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
  def helper(p, q):
    if p and q:
      return p.val == q.val and helper(p.left, q.right) and helper(p.right, q.left)
    else:
      return p is q
  return helper(root, root)
```

{% endtab %}{% endtabs %}
