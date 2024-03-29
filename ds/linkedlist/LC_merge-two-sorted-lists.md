# [LC_merge-two-sorted-lists](https://leetcode.com/problems/merge-two-sorted-lists)

* en

  ```en
  Merge two linked lists

  ```

* tc

  ```tc
  Input: l1 = [1,2,4], l2 = [1,3,4]
  Output: [1,1,2,3,4,4]
  ```

## Solution

* cpp

  ```cpp
  ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
    ListNode dummy(INT_MIN);
    ListNode *tail = &dummy;
    while (l1 && l2) {
      if (l1->val < l2->val) {
        tail->next = l1;
        l1 = l1->next;
      } else {
        tail->next = l2;
        l2 = l2->next;
      }
      tail = tail->next;
    }

    tail->next = l1 ? l1 : l2;
    return dummy.next;
  }
  ```

* py

  ```py
  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = cur = ListNode(0)
    while l1 and l2:
      if l1.val < l2.val:
        cur.next = l1
        l1 = l1.next
      else:
        cur.next = l2
        l2 = l2.next
      cur = cur.next
    cur.next = l1 or l2
    return dummy.next
  ```
