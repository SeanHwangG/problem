{% tabs %}{% tab title='LC_512.sql' %}

```sql
SELECT DISTINCT player_id, first_value(device_id) OVER (PARTITION BY player_id ORDER BY event_date) device_id FROM activity
```

{% endtab %}{% endtabs %}
