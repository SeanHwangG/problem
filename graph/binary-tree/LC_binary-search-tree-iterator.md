# [LC_binary-search-tree-iterator](https://leetcode.com/problems/binary-search-tree-iterator)

* en

  ```en
  Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
  BSTIterator(TreeNode root) Initializes an object of the BSTIterator class
    The pointer should be initialized to a non-existent number smaller than any element in the BST
  boolean hasNext() Returns true if there exists a number in traversal to right of pointer, otherwise returns false
  int next() Moves the pointer to the right, then returns the number at the pointer
  ```

* tc

  ```tc
  Input:
  ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
  [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]

  Output: [null, 3, 7, true, 9, true, 15, true, 20, false]
  ```

## Solution

* py

  ```py
  class BSTIterator(object):
    def __init__(self, root):
      self.root_node=root
      self.current_node=root
      self.stack=[]

    def hasNext(self):
      return self.current_node is not None or self.stack

    def next(self):
      while self.current_node:
        self.stack.append(self.current_node)
        self.current_node=self.current_node.left
      next=self.stack.pop()
      self.current_node=next.right
      return next.val
  ```
