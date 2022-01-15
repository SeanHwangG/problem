{% tabs %}{% tab title='LC_931.py' %}

```py
def minFallingPathSum(self, A):
  dp = A[0]
  for row in A[1:]:
    dp = [value + min(dp[max(0, c - 1) : c + 2]) for c, value in enumerate(row)]
  return min(dp)
```

{% endtab %}{% endtabs %}
