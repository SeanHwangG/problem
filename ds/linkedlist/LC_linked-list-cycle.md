# [LC_linked-list-cycle](https://leetcode.com/problems/linked-list-cycle)

* en

  ```en
  Check if linkedlist has cycle
  ```

* tc

  ```tc
  Input: head = [3,2,0,-4], pos = 1
  Output: true
  ```

## Solution

* py

  ```py
  def hasCycle(self, head):
    try:
      slow = head
      fast = head.next
      while slow is not fast:
        slow = slow.next
        fast = fast.next.next
      return True
    except:
      return False
  ```
