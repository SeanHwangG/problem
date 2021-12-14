{% tabs %}{% tab title='LC_1400.py' %}

```py
def canConstruct(self, s, k):
  return sum(i & 1 for i in collections.Counter(s).values()) <= k <= len(s)
```

{% endtab %}{% endtabs %}
