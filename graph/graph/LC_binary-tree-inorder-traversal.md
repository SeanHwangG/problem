# [LC_binary-tree-inorder-traversal](https://leetcode.com/problems/binary-tree-inorder-traversal)

* en

  ```en
  Given root of binary tree, return inorder traversal of its nodes' values
  ```

* tc

  ```tc
  Input: root = [1,null,2,3]
  Output: [1,3,2]
  ```

## Solution

* go

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

* py
  * Time: O(n)
  * Space: O(n)

  ```py
  def inorderTraversal(self, root):
    return self.inorderTraversal(root.left)+[root.val] + self.inorderTraversal(root.right) if root else []
  ```
