{% tabs %}{% tab title='LC_1987.py' %}

```py
def numberOfUniqueGoodSubsequences(self, b: str) -> int:
  mod = 10**9 + 7
  dp = [0, 0]
  for c in b:
    dp[int(c)] = (sum(dp) + int(c)) % mod
  return (sum(dp) + ('0' in b)) % mod
```

{% endtab %}{% endtabs %}
