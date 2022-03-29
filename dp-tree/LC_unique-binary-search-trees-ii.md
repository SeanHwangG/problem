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
