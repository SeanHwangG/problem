{% tabs %}{% tab title='LC_614.sql' %}

```sql
SELECT DISTINCT f.follower, f3.num FROM follow f
  JOIN (SELECT f2.followee, COUNT(DISTINCT f2.follower) AS "num"
        FROM follow f2 GROUP BY f2.followee) f3
  ON f.follower = f3.followee ORDER BY f.follower
```

{% endtab %}{% endtabs %}
