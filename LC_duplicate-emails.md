{% tabs %}{% tab title='LC_182.sql' %}

```sql
SELECT email FROM Person
  GROUP BY email HAVING count(*) > 1;
```

{% endtab %}{% endtabs %}
