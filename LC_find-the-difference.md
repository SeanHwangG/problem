{% tabs %}{% tab title='LC_389.py' %}

```py
def findTheDifference(self, s: str, t: str) -> str:
  return chr(reduce(operator.xor, map(ord, s + t)))
```

{% endtab %}{% endtabs %}
