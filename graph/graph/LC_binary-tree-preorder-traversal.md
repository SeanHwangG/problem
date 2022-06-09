# [LC_binary-tree-preorder-traversal](https://leetcode.com/problems/binary-tree-preorder-traversal)

* en

  ```en
  Given the root of a binary tree, return the preorder traversal of its nodes' values
  ```

* tc

  ```tc
  Input: root = [1,null,2,3]
  Output: [1,2,3]
  ```

## Solution

* py

  ```py
  def preorderTraversal(self, root):
    ret, stack = [], [root]
    while stack:
      node = stack.pop()
      if node:
        ret.append(node.val)
        stack.extend([node.right, node.left])
    return ret
  ```
