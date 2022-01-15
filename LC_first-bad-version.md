{% tabs %}{% tab title='LC_278.py' %}

```py
def firstBadVersion(self, n):
  lo, hi = 1, n
  while lo < hi:
    mi = (lo + hi) // 2
    if not isBadVersion(mi):
      lo = mi + 1
    else:
      hi = mi
  return lo
```

{% endtab %}{% endtabs %}
