# [LC_reorder-list](https://leetcode.com/problems/reorder-list)

* en

  ```en
  Given head of a singly linked-list. The list can be represented as:
    Reorder the list to be on the following form:
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
  ```

* tc

  ```tc
  Input: head = [1,2,3,4]
  Output: [1,4,2,3]
  ```

## Solution

* py

  ```py
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
    def reorderList(self, head):
      # find the mid point
      slow = fast = head
      while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

      # reverse the second half in-place
      pre, node = None, slow
      while node:
        pre, node.next, node = node, pre, node.next

      # Merge in-place; Note : the last node of "first" and "second" are the same
      first, second = head, pre
      while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
  ```
