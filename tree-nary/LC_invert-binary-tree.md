# [LC_invert-binary-tree](https://leetcode.com/problems/invert-binary-tree)

Invert binary tree

```txt
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

## Solution

* Recursive

  ```py
  def invertTree(self, root):
    if root:
      root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root
  ```

* Iterative

  ```py
  def invertTree(self, root):
    stack = [root]
    while stack:
      node = stack.pop()
      if node:
        node.left, node.right = node.right, node.left
        stack += node.left, node.right
    return root
  ```
