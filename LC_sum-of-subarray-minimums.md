{% tabs %}{% tab title='LC_907.py' %}

```py
def sumSubarrayMins(self, A):
  res, s = 0, []
  A = [0] + A + [0]
  for i, x in enumerate(A):
    while s and A[s[-1]] > x:
      j = s.pop()
      k = s[-1]
      res += A[j] * (i - j) * (j - k)
    s.append(i)
  return res % (10**9 + 7)
```

{% endtab %}{% endtabs %}
