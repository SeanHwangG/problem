{% tabs %}{% tab title='LC_1050.sql' %}

```sql
SELECT actor_id, director_id FROM ActorDirector
  GROUP BY actor_id, director_id HAVING COUNT(1) >= 3
```

{% endtab %}{% endtabs %}
