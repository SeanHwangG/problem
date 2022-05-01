# [LC_count-complete-tree-nodes](https://leetcode.com/problems/count-complete-tree-nodes)

Given root of complete binary tree, return # of nodes in tree in less than O(n) time
Every level, except last, is completely filled in a complete binary tree, and all nodes in last level are as far left
It can have between 1 and 2h nodes inclusive at the last level h

```txt
Input: root = [1,2,3,4,5,6]
Output: 6

Input: root = [1]
Output: 1
```

## Solution

* Time; O(log^2 N) (Master Theorem)
* Space; O(log(n))

* py

  ```py
  def countNodes(self, root):
    def getDepth(root):
      if not root:
        return 0
      return 1 + getDepth(root.left)
    if not root:
      return 0
    l_depth = getDepth(root.left)
    r_depth = getDepth(root.right)
    if l_depth == r_depth:
      return pow(2, l_depth) + self.countNodes(root.right)
    else:
      return pow(2, r_depth) + self.countNodes(root.left)

  ```
