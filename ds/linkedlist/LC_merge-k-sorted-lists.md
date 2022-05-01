# [LC_merge-k-sorted-lists](https://leetcode.com/problems/merge-k-sorted-lists)

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

```txt
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

## Solution

* py

  ```py
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  def mergeKLists(self, lists):
    def vals(node):
      while node:
        yield node.val
        node = node.next
    dummy = last = ListNode(None)
    for val in heapq.merge(*map(vals, lists)):
      last.next = last = ListNode(val)
    return dummy.next
  ```
