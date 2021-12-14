{% tabs %}{% tab title='LC_1526.py' %}

```py
def minNumberOperations(self, A: List[int]) -> int:
  return sum(max(b - a, 0) for b, a in zip(A, [0] + A))
```

{% endtab %}{% endtabs %}
