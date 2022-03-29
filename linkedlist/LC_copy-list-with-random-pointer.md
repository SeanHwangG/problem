```py
class Solution:
  def copyRandomList(self, head: 'Node') -> 'Node':
    node = head
    while node:
      node.random, node = Node(node.val, node.random, None), node.next
    # populate random field of the new node
    node = head
    while node:
      node.random.random, node = node.random.next.random if node.random.next else None, node.next
    # restore original list and build new list
    head_copy, node = head.random if head else None, head
    while node:
      node.random.next, node.random, node = node.next.random if node.next else None, node.random.next, node.next
    return head_copy
```
