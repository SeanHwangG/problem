{% tabs %}{% tab title='LC_206.js' %}

```js
var reverseList = function(head) {
  let [prev, current] = [null, head]
  while (current) {
    [current.next, prev, current] = [prev, current, current.next]
  }
  return prev
}
```

{% endtab %}{% tab title='LC_206.py' %}

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

{% endtab %}{% endtabs %}