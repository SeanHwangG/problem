{% tabs %}{% tab title='LC_602.sql' %}

```sql
SELECT union_table.requester_id AS "id", COUNT(*) AS "num"
  FROM (SELECT r.requester_id FROM request_accepted r
        UNION ALL (SELECT r2.accepter_id FROM request_accepted r2)) union_table
  GROUP BY union_table.requester_id
  ORDER BY num DESC LIMIT 1
```

{% endtab %}{% endtabs %}
