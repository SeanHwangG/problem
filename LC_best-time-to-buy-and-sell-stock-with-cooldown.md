{% tabs %}{% tab title='LC_309.cpp' %}

```cpp
int maxProfit(vector<int>& prices) {
  if (prices.size() == 0) return 0;
  int cool = 0, nocool = 0, buy = -prices[0];
  for (int i = 1; i < prices.size(); i++){
    buy = max(nocool - prices[i], buy);
    nocool = max(nocool, cool);
    cool = buy + prices[i];
  }
  return max(cool, nocool);
}
```

{% endtab %}{% endtabs %}
