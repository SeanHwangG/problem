{% tabs %}{% tab title='HR_weather-observation-station-4.sql' %}

```sql
SELECT COUNT(City) - COUNT(DISTINCT City) FROM Station;
```

{% endtab %}{% endtabs %}
