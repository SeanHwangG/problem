# [LC_linked-list-cycle-ii](https://leetcode.com/problems/linked-list-cycle-ii)

Given a linked list, return the node where the cycle begins. If there is no cycle, return null

```txt
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
```

## Solution

* py

  ```py
  def detectCycle(self, head):
    try:
      fast = head.next
      slow = head
      while fast is not slow:
        fast = fast.next.next
        slow = slow.next
    except:
      return None

    slow = slow.next
    while head is not slow:
      head = head.next
      slow = slow.next
    return head
  ```
