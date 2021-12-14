{% tabs %}{% tab title='LC_534.sql' %}

```sql
SELECT A1.player_id, A1.event_date, SUM(A2.games_played) AS 'games_played_so_far' FROM Activity A1
  LEFT JOIN Activity A2 ON A1.player_id = A2.player_id and A1.event_date >= A2.event_date
  GROUP BY A1.player_id, A1.event_date
```

{% endtab %}{% endtabs %}
