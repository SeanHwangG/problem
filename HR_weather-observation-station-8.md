{% tabs %}{% tab title='HR_weather-observation-station-8.sql' %}

```sql
SELECT DISTINCT city FROM station
  WHERE city REGEXP '^[aeiou].*[aeiou]$'
```

{% endtab %}{% endtabs %}
