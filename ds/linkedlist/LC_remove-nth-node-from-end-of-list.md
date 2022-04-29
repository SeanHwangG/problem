# [LC_remove-nth-node-from-end-of-list](https://leetcode.com/problems/remove-nth-node-from-end-of-list)

Remove nth node from end

```txt
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

## Solution

```cpp
class Solution {
public:
  ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode* node = head, *offsetNode = head;
    for (int i = 0; i < n; ++i) node = node->next;
    if (node == NULL) return head->next;
    while (node->next != NULL) {
      node = node->next;
      offsetNode = offsetNode->next;
    }
    offsetNode->next = offsetNode->next->next;
    return head;
  }
};
```

```py
def removeNthFromEnd(self, head, n):
  fast = slow = head
  for _ in range(n):
    fast = fast.next
  if not fast:
    return head.next
  while fast.next:
    fast = fast.next
    slow = slow.next
  slow.next = slow.next.next
  return head
```
