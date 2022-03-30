```java
public ListNode reverseList(ListNode head) {
  if(head == null || head.next == null)  return head;
  ListNode reversedHead = reverseList(head.next);
  head.next.next = head;
  head.next = null;
  return reversedHead;
}
```

```js
var reverseList = function(head) {
  let [prev, current] = [null, head]
  while (current) {
    [current.next, prev, current] = [prev, current, current.next]
  }
  return prev
}
```

```py
def reverseList(self, head: ListNode) -> ListNode:
  if head == None:
    return None
  prev = None
  while head.next != None:
    nxt = head.next
    head.next = prev
    prev, head = head, nxt
  head.next = prev
  return head
```