{% tabs %}{% tab title='LC_197.py' %}

```sql
SELECT weather.id AS 'Id' FROM weather
  JOIN weather w ON DATEDIFF(weather.recordDate, w.recordDate) = 1
    AND weather.Temperature > w.Temperature;
```

{% endtab %}{% endtabs %}
