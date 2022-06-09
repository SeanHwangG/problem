# [LC_binary-tree-postorder-traversal](https://leetcode.com/problems/binary-tree-postorder-traversal)

* en

  ```en
  Given root of a binary tree, return postorder traversal of its nodes' values
  ```

* tc

  ```tc
  Input: root = [1,null,2,3]
  Output: [3,2,1]
  ```

## Solution

* py

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
