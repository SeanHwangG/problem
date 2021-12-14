{% tabs %}{% tab title='LC_121.java' %}

```java
public int maxProfit(int[] prices) {
  if (prices.length < 2)  return 0;
  int maxProfit = 0, min = prices[0];
  for (int i = 1; i < prices.length; i++){
    if (min > prices[i]) min = prices[i];
    else maxProfit = prices[i] - min > maxProfit? prices[i] - min: maxProfit;
  }
  return maxProfit;
}
```

{% endtab %}{% endtabs %}
