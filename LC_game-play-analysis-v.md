{% tabs %}{% tab title='LC_1097.py' %}

```sql
SELECT a.event_date AS "install_dt",
       COUNT(DISTINCT a.player_id) AS "installs",
       CAST(AVG(CASE WHEN a3.games_played > 0 THEN 1 ELSE 0 END) AS decimal(16,2)) AS "Day1_retention"
  FROM ((SELECT a2.player_id, MIN(a2.event_date) AS "event_date" FROM Activity a2 GROUP BY a2.player_id)) a
    LEFT JOIN Activity a3 ON a3.player_id = a.player_id AND a3.event_date = DATE_ADD(a.event_date, INTERVAL 1 DAY)
  GROUP BY a.event_date
```

{% endtab %}{% endtabs %}
