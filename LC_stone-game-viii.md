{% tabs %}{% tab title='LC_1872.py' %}

```py
def stoneGameVIII(self, stones):
  ans = sum(stones)
  for num in list(accumulate(stones))[::-1][1:-1]:
    ans = max(ans, num - ans)
  return ans
```

{% endtab %}{% endtabs %}
