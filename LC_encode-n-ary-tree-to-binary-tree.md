```py
"""
class Node:
  def __init__(self, val=None, children=None):
    self.val, self.children = val, children

class TreeNode:
  def __init__(self, x):
    self.val, self.left, self.right = x, None, None
"""

class Codec:
  def encode(self, root):
    if not root:
      return None
    binary = TreeNode(root.val)
    if not root.children:
      return binary
    binary.left = self.encode(root.children[0])
    node = binary.left  # Left child of binary is encoding of all n-ary children starting with first child
    for child in root.children[1:]:  # Other children of n-ary root are right child of previous child
      node.right = self.encode(child)
      node = node.right
    return binary

  def decode(self, data):
    if not data:
      return None
    nary, node = Node(data.val, []), data.left
    while node:                                 # While more children of n-ary root
      nary.children.append(self.decode(node))   # Append to list and move to next child
      node = node.right
    return nary
```
