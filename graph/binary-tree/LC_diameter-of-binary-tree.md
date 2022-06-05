# [LC_diameter-of-binary-tree](https://leetcode.com/problems/diameter-of-binary-tree)

```en
Find diameter of binary tree
```

```txt
Input: root = [1,2,3,4,5]
Output: 3
```

## Solution

* py

  ```py
  def diameterOfBinaryTree(self, root):
    self.ans = 0

    def depth(p):
      if not p: return 0
      left, right = depth(p.left), depth(p.right)
      self.ans = max(self.ans, left+right)
      return 1 + max(left, right)

    depth(root)
    return self.ans
  ```
