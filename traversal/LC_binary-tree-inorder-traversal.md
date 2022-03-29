```go
func inorderTraversal(root *TreeNode) []int {
  var xs []int
  if root != nil {
    xs = append(xs, inorderTraversal(root.Left)...)
    xs = append(xs, root.Val)
    xs = append(xs, inorderTraversal(root.Right)...)
  }
  return xs
}
```

* Time: O(n)
* Space: O(n)

```py
def inorderTraversal(self, root):
  return self.inorderTraversal(root.left)+[root.val] + self.inorderTraversal(root.right) if root else []
```
