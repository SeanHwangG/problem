# [LC_symmetric-tree](https://leetcode.com/problems/symmetric-tree)

Given root of binary tree, check whether it is mirror of itself

```txt
Input: root = [1,2,2,3,4,4,3]
Output: true
```

## Solution

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

```py
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
  def helper(p, q):
    if p and q:
      return p.val == q.val and helper(p.left, q.right) and helper(p.right, q.left)
    else:
      return p is q
  return helper(root, root)
```
