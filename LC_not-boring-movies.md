{% tabs %}{% tab title='LC_620.sql' %}

```sql
SELECT * FROM cinema
  WHERE description != 'boring' AND id % 2 = 1
  ORDER BY rating DESC;
```

{% endtab %}{% endtabs %}
