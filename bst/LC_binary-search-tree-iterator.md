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
