{% tabs %}{% tab title='LC_627.sql' %}

```sql
UPDATE salary SET sex =
  CASE sex
    WHEN 'f' THEN 'm'
    WHEN 'm' THEN 'f'
  END
```

{% endtab %}{% endtabs %}
