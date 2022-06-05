# [LC_convert-bst-to-greater-tree](https://leetcode.com/problems/convert-bst-to-greater-tree)

```en
Given the root of a BST, convert it to a Greater Tree
st every key of original BST is changed to original key plus sum of all keys greater than the original key in BST
```

```txt
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
```

## Solution

* py

  ```py
  class Solution:
    def __init__(self):
      self.total = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
      if not root:
        return
      self.convertBST(root.right)
      root.val += self.total
      self.total = root.val
      self.convertBST(root.left)
      return root
  ```
