{% tabs %}{% tab title='LC_100.py' %}

```py
def isSameTree(self, p, q):
  if p and q:
    return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
  return p is q
```

{% endtab %}{% endtabs %}