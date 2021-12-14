{% tabs %}{% tab title='LC_1070.sql' %}

```sql
SELECT s2.product_id, s2.year AS "first_year", s2.quantity, s2.price FROM Sales s2
  JOIN (SELECT s.product_id, MIN(s.year) AS "year" FROM Sales s
        GROUP BY s.product_id ) first_year
  ON s2.product_id = first_year.product_id AND s2.year = first_year.year
```

{% endtab %}{% endtabs %}
