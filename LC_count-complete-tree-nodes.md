* Time; O(log^2 N) (Master Theorem)
* Space; O(log(n))

```py
def countNodes(self, root):
  def getDepth(root):
    if not root:
      return 0
    return 1 + getDepth(root.left)
  if not root:
    return 0
  l_depth = getDepth(root.left)
  r_depth = getDepth(root.right)
  if l_depth == r_depth:
    return pow(2, l_depth) + self.countNodes(root.right)
  else:
    return pow(2, r_depth) + self.countNodes(root.left)

```
