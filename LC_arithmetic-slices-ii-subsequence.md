{% tabs %}{% tab title='LC_446.py' %}

```py
def numberOfArithmeticSlices(self, li: List[int]) -> int:
  ans = 0
  dp = defaultdict(int)
  for i in range(1, len(li)):
    for j in range(i):
      delta = li[i] - li[j]
      ans += dp[(j, delta)]
      dp[(i, delta)] += dp[(j, delta)] + 1

  return ans
```

{% endtab %}{% endtabs %}
