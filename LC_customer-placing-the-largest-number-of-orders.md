{% tabs %}{% tab title='LC_586.sql' %}

```sql
SELECT  customer_number FROM orders
  GROUP BY customer_number
  ORDER BY COUNT(order_number) DESC LIMIT 1
```

{% endtab %}{% endtabs %}
