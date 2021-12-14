{% tabs %}{% tab title='LC_153.py' %}

```py
def findMin(self, li):
  lo, hi = 0, len(li) - 1
  while lo < hi:
    mi = (lo + hi) // 2
    if li[mi] > li[hi]:
      lo = mi + 1
    else:
      hi = mi
  return li[lo]
```

{% endtab %}{% endtabs %}
