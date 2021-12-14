{% tabs %}{% tab title='LC_552.py' %}

```py
class Solution(object):
  def checkRecord(self, N):
    MOD = 10 ** 9 + 7
    a = b = d = 1  # without an 'A' ending in N, NL, LL
    c = e = f = 0  # with an 'A' ending in N, NL, LL
    for _ in range(N-1):
      a, b, c, d, e, f = (a + b + c) % MOD, a, b, (a + b + c + d + e + f) % MOD, d, e
    return (a + b + c + d + + e + f) % MOD
```

{% endtab %}{% endtabs %}
