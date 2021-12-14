{% tabs %}{% tab title='LC_1667.sql' %}

```sql
SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS 'name'
  FROM Users
  ORDER BY user_id ASC
```

{% endtab %}{% endtabs %}
