{% tabs %}{% tab title='LC_1310.py' %}

```py
def xorQueries(self, A, queries):
  for i in range(len(A) - 1):
    A[i + 1] ^= A[i]
  return [A[j] ^ A[i - 1] if i else A[j] for i, j in queries]
```

{% endtab %}{% endtabs %}
