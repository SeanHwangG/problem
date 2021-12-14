{% tabs %}{% tab title='LC_23.py' %}

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

{% endtab %}{% endtabs %}
