# [LC_middle-of-the-linked-list](https://leetcode.com/problems/middle-of-the-linked-list)

* en

  ```en
  Print middle node in linked list
  ```

* tc

  ```tc
  Input: [1,2,3,4,5,6]
  Output: Node 4 from this list (Serialization: [4,5,6])
  ```

## Solution

* py

  ```py
  def middleNode(self, head: ListNode) -> ListNode:
    slow, fast = head, head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    return slow
  ```
