{% tabs %}{% tab title='LC_431.md' %}

* Design an algorithm to encode an N-ary tree into a binary tree and decode binary tree to get original N-ary tree

```txt
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
```

{% endtab %}{% tab title='LC_431.py' %}

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

{% endtab %}{% endtabs %}
