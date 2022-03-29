```py
def preorderTraversal(self, root):
  ret, stack = [], [root]
  while stack:
    node = stack.pop()
    if node:
      ret.append(node.val)
      stack.extend([node.right, node.left])
  return ret
```
