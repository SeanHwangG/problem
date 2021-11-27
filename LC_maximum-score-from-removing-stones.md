{% tabs %}{% tab title='LC_1753.py' %}

```py
def maximumScore(self, a: int, b: int, c: int) -> int:
  a, b, c = sorted([a, b, c])
  return (a + b + c) // 2 if a + b >= c else a + b
```

{% endtab %}{% endtabs %}
