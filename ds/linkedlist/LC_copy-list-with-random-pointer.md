# [LC_copy-list-with-random-pointer](https://leetcode.com/problems/copy-list-with-random-pointer)

* en

  ```en
  Linked list of length n is given ST each node contains random pointer, which could point to any node in list, or null
  Construct a deep copy of the list
  ```

* tc

  ```tc
  Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
  Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
  ```

## Solution

* py

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
