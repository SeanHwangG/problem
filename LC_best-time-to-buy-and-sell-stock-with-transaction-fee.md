{% tabs %}{% tab title='LC_714.py' %}

```py
def maxProfit(self, prices, fee):
  cash, hold = 0, -prices[0]
  for i in range(1, len(prices)):
    cash = max(cash, hold + prices[i] - fee)
    hold = max(hold, cash - prices[i])
  return cash
```

{% endtab %}{% endtabs %}
