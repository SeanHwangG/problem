# [LC_maximum-depth-of-binary-tree](https://leetcode.com/problems/maximum-depth-of-binary-tree)

* en

  ```en
  Given root of binary tree, return its maximum depth
  ```

* tc

  ```tc
  Input: root = [3,9,20,null,null,15,7]
  Output: 3

  Input: root = [1,null,2]
  Output: 2
  ```

## Solution

* go

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
