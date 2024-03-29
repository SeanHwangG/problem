# [LC_binary-tree-cameras](https://leetcode.com/problems/binary-tree-cameras)

* en

  ```en
  Each camera at a node can monitor its parent, itself, and its immediate children
  Print minimum number of cameras
  ```

* tc

  ```tc
  Input: [0,0,null,0,0]
  Output: 1
  ```

## Solution

* py

  ```py
  def minCameraCover(self, root):
    self.res = 0
    def dfs(root):
      if not root: return 2
      l, r = dfs(root.left), dfs(root.right)
      if l == 0 or r == 0:
        self.res += 1
        return 1
      return 2 if l == 1 or r == 1 else 0
    return (dfs(root) == 0) + self.res
  ```
