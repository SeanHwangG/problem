# [LC_unique-binary-search-trees-ii](https://leetcode.com/problems/unique-binary-search-trees-ii)

* en

  ```en
  Given an integer n, return all the structurally unique BST's, which has exactly n nodes of unique values from 1-n
  ```

* tc

  ```tc
  Input: n = 3
  Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
  ```

## Solution

* py

  ```py
  def node(val, left, right):
    node = TreeNode(val)
    node.left, node.right = left, right
    return node

  def generateTrees(self, last, first=1):
    return [node(root, left, right)
            for root in range(first, last+1)
            for left in self.generateTrees(root-1, first)
            for right in self.generateTrees(last, root+1)] or [None]
  ```
