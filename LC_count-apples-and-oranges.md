{% tabs %}{% tab title='LC_1715.py' %}

```sql
SELECT sale_date, sum(CASE WHEN fruit='apples' THEN sold_num ELSE -sold_num END) AS diff FROM Sales
  GROUP BY sale_date
```

{% endtab %}{% endtabs %}
