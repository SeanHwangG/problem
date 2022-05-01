# [LC_distribute-coins-in-binary-tree](https://leetcode.com/problems/distribute-coins-in-binary-tree)

Given root of a binary tree with n nodes where each node in tree has node.val coins
There are n coins in total throughout the whole tree.
In one move, choose two adjacent nodes and move one coin from one node to another
A move may be from parent to child, or from child to parent.
Return min number of moves required to make every node have exactly one coin

```txt
Input: root = [3,0,0]
Output: 2

Input: root = [1,0,0,null,3]
Output: 4
```

## Solution

* py

  ```py
  res = 0
  def distributeCoins(self, root):
    def dfs(root):
      if not root: return 0
      left = dfs(root.left)
      right = dfs(root.right)
      self.res += abs(left) + abs(right)
      return root.val + left + right - 1
    dfs(root)
    return self.res
  ```
