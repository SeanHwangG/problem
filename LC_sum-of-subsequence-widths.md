{% tabs %}{% tab title='LC_891.py' %}

```py
def sumSubseqWidths(self, A: List[int]) -> int:
  A.sort()
  res = 0
  for i in range(len(A)):
    res *= 2
    res += A[~i] - A[i]
    res %= 10 ** 9 + 7
  return res
```

{% endtab %}{% endtabs %}
