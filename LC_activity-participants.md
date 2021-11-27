{% tabs %}{% tab title='LC_1355.sql' %}

```sql
WITH activity_count AS (
    SELECT f.activity, COUNT(1) AS 'act_counts' FROM Friends f
    GROUP BY f.activity)

SELECT a.activity FROM activity_count a
  WHERE a.act_counts != (SELECT MAX(act_counts) FROM activity_count)
  AND a.act_counts != (SELECT MIN(act_counts) FROM activity_count)
```

{% endtab %}{% endtabs %}
