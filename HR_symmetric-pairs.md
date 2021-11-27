{% tabs %}{% tab title='HR_symmetric-pairs.sql' %}

```sql
SELECT x, y FROM functions f1
  WHERE exists(SELECT * FROM functions f2 WHERE f2.y=f1.x
  AND f2.x=f1.y AND f2.x>f1.x) AND (x!=y) UNION
SELECT x, y FROM functions f1 WHERE x=y AND
  ((SELECT count(*) FROM functions WHERE x=f1.x AND y=f1.x) > 1) ORDER BY x;
```

{% endtab %}{% endtabs %}
