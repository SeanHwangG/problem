# [LC_delete-node-in-a-bst](https://leetcode.com/problems/delete-node-in-a-bst)

* en

  ```en
  Given a root node reference of a BST and a key, delete the node with the given key in the BST
  Return root node reference (possibly updated) of the BST
  ```

* tc

  ```tc
  Input: root = [5,3,6,2,4,null,7], key = 3
  Output: [5,4,6,2,null,null,7]

  ```

## Solution

* py

  ```py
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
      if not root: # Root doesn't exist, just return it
        return root
      if root.val > key: # key is less than root value, find node in left subtree
        root.left = self.deleteNode(root.left, key)
      elif root.val < key: # key is greater than root value, find node in right subtree
        root.right= self.deleteNode(root.right, key)
      else: # Found node (root.value == key), start to delete it
        if not root.right: # if no right children, we delete node then new root would be root.left
          return root.left
        if not root.left: # if no left children, we delete node then new root would be root.right
          return root.right
        # if both children, replace with min value in right subtree then delete that min node in right subtree
        temp, mn = root.right, root.right.val
        while temp.left:
          temp = temp.left
          mn = temp.val
        root.val = mn # replace value
        root.right = self.deleteNode(root.right,root.val) # delete minimum node in right subtree
      return root
  ```
