{% tabs %}{% tab title='LC_1045.sql' %}

```sql
SELECT customer_id FROM (SELECT * FROM Customer WHERE product_key in (SELECT * FROM Product)) AS A
  GROUP BY customer_id
  HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(product_key) FROM Product)
```

{% endtab %}{% endtabs %}
