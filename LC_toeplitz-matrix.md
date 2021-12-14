{% tabs %}{% tab title='LC_766.py' %}

```py
def isToeplitzMatrix(self, m):
  return all(r1[:-1] == r2[1:] for r1, r2 in zip(m, m[1:]))
```

{% endtab %}{% endtabs %}
