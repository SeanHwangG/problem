# [LC_kth-smallest-element-in-a-bst](https://leetcode.com/problems/kth-smallest-element-in-a-bst)

* en

  ```en
  Given root of binary search tree, and an integer k, return kth (1-indexed) smallest element in the tree
  ```

* tc

  ```tc
  Input: root = [5,3,6,2,4,null,null,1], k = 3
  Output: 3
  ```

## Solution

* py

  ```py
  class Solution(object):
    def kthSmallest(self, root: TreeNode, k: int):
      count = []
      self.helper(root, count)
      return count[k-1]

    def helper(self, node, count):
      if not node: return
      self.helper(node.left, count)
      count.append(node.val)
      self.helper(node.right, count)
  ```
