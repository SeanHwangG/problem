# [LC_closest-binary-search-tree-value-ii](https://leetcode.com/problems/closest-binary-search-tree-value-ii)

* en

  ```en
  Given root of a binary search tree, a target value, and an integer k, return k values in BST that are closest to target
  Return answer in any order, are guaranteed to have only one unique set of k values in BST that are closest to target
  ```

* tc

  ```tc
  Input: root = [4,2,5,1,3], target = 3.714286, k = 2
  Output: [4,3]
  ```

## Solution

* py

  ```py
  def closestKValues(self, root, target, k):
    def vals(root):
      return vals(root.left) + [root.val] + vals(root.right) if root else []
    return sorted(vals(root), key=lambda x: abs(x - target))[:k]
  ```
