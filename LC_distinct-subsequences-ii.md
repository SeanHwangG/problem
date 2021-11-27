{% tabs %}{% tab title='LC_940.py' %}

```py
def distinctSubseqII(self, S):
  res, end = 0, collections.Counter()
  for c in S:
    res, end[c] = res * 2 + 1 - end[c], res + 1
  return res % (10 ** 9 + 7)
```

{% endtab %}{% endtabs %}
