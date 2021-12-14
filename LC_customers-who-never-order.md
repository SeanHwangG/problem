{% tabs %}{% tab title='LC_183.sql' %}

```sql
SELECT A.Name from Customers A
  WHERE NOT EXISTS (SELECT 1 FROM Orders B WHERE A.Id = B.CustomerId limit 1)
```

{% endtab %}{% endtabs %}
