{% tabs %}{% tab title='LC_1809.sql' %}

```sql
SELECT p.session_id FROM Playback p
  LEFT JOIN Ads a ON a.timestamp BETWEEN p.start_time AND p.end_time AND p.customer_id = a.customer_id
  WHERE a.ad_id IS NULL
```

{% endtab %}{% endtabs %}
