# [LC_convert-sorted-list-to-binary-search-tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree)

* en

  ```en
  Make BST from sorted linked list
  ```

* tc

  ```tc
  Input: head = [-10,-3,0,5,9]
  Output: [0,-3,9,-10,null,5]
  ```

## Solution

* py

  ```py
  def sortedListToBST(self, head):
    if not head:
      return
    if not head.next:
      return TreeNode(head.val)

    slow, fast = head, head.next.next
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
    tmp = slow.next

    slow.next = None
    root = TreeNode(tmp.val)
    root.left = self.sortedListToBST(head)
    root.right = self.sortedListToBST(tmp.next)
    return root
  ```
