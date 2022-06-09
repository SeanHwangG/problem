# [LC_rotate-list](https://leetcode.com/problems/rotate-list)

* en

  ```en
  Given the head of a linked list, rotate the list to the right by k places
  ```

* tc

  ```tc
  Input: head = [1,2,3,4,5], k = 2
  Output: [4,5,1,2,3]
  ```

## Solution

* py

  ```py
  def rotateRight(self, head: ListNode, k: int) -> ListNode:
    if not head:
      return None
    old_last = head
    length = 1
    while old_last.next:
      old_last = old_last.next
      length += 1
    k = k % length
    old_last.next = head
    new_last = head
    for _ in range(length - k - 1):
      new_last = new_last.next
    answer = new_last.next
    new_last.next = None
    return answer
  ```
