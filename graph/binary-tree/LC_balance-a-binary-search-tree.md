# [LC_balance-a-binary-search-tree](https://leetcode.com/problems/balance-a-binary-search-tree)

* en

  ```en
  Given a binary search tree, return a balanced binary search tree with the same node values
  Binary search tree is balanced iff the depth of the two subtrees of every node never differ by more than 1
  ```

* tc

  ```tc
  Input: root = [1,null,2,null,3,null,4,null,null]
  Output: [2,1,3,null,null,null,4]
  ```

## Solution

* py

  ```py
  class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

      def dfs(node):
        if not node: return []
        return dfs(node.left) + [node.val] + dfs(node.right)
      ns = dfs(root)

      def build(l, r):
        if l > r: return None
        m = (l + r) // 2
        root = TreeNode(ns[m])
        root.left, root.right = build(l, m-1), build(m + 1, r)
        return root

      return build(0, len(ns) - 1)
  ```
