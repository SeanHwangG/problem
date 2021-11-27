{% tabs %}{% tab title='LC_626.sql' %}

```sql
SELECT
  IF(id < (SELECT count(*) from seat), IF(id MOD 2=0, id-1, id+1), IF(id MOD 2=0, id-1, id)) as id, student
FROM seat ORDER BY id asc;
```

{% endtab %}{% endtabs %}
