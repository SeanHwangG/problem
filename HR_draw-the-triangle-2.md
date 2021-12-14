{% tabs %}{% tab title='HR_draw-the-triangle-2.sql' %}

```sql
SELECT REPEAT('* ', @NUMBER:= @NUMBER + 1) FROM information_schema.tables, (SELECT @NUMBER:=0) t LIMIT 20
```

{% endtab %}{% endtabs %}
