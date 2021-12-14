{% tabs %}{% tab title='LC_1785.py' %}

```py
def minElements(self, A, limit, goal):
  return (abs(sum(A) - goal) + limit - 1) / limit
```

{% endtab %}{% endtabs %}
