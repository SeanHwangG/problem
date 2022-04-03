# [LC_design-linked-list](https://leetcode.com/problems/design-linked-list)

Implement the MyLinkedList class:
MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list
  After the insertion, new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list
  If index equals length of linked list, node will be appended to end of linked list
  If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid


```txt
Input:
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]

Output:
[null, null, null, null, 2, null, 3]
```

## Solution

```py
class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None


class MyLinkedList(object):
  def __init__(self):
    self.head, self.size = None, 0

  def get(self, index: int) -> int:
    if index < 0 or index >= self.size:
      return -1

    current = self.head

    for _ in range( index):
      current = current.next

    return current.val

  def addAtHead(self, val: int) -> None:
    self.addAtIndex(0, val)

  def addAtTail(self, val: int) -> None:
    self.addAtIndex(self.size, val)

  def addAtIndex(self, index: int, val: int) -> None:
    if index > self.size:
      return

    current = self.head
    new_node = ListNode(val)

    if index <= 0:
      new_node.next = current
      self.head = new_node
    else:
      for _ in range(index - 1):
        current = current.next
      new_node.next = current.next
      current.next = new_node

    self.size += 1

  def deleteAtIndex(self, index: int) -> None:
    if index < 0 or index >= self.size:
      return

    current = self.head

    if index == 0:
      self.head = self.head.next
    else:
      for _ in range(index - 1):
        current = current.next
      current.next = current.next.next

    self.size -= 1
```
