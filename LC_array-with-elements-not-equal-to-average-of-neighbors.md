{% tabs %}{% tab title='LC_1968.py' %}

```py
def rearrangeArray(self, A: list):
  A.sort()
  for i in range(1, len(A), 2):
    A[i], A[i - 1] = A[i - 1], A[i]
  return A
```

{% endtab %}{% endtabs %}
