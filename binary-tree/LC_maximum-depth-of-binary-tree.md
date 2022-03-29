```go
func maxDepth(root *TreeNode) int {
  if root == nil {
    return 0
  }
  return 1 + max(maxDepth(root.Left), maxDepth(root.Right))
}

func max(l, r int) int {
  if l > r {
    return l
  }
  return r
}
```
