{% tabs %}{% tab title='HR_weather-observation-station-13.sql' %}

```sql
SELECT TRUNCATE(SUM(LAT_N), 4) FROM Station
  WHERE LAT_N > 38.7880 AND LAT_N < 137.2345;
```

{% endtab %}{% endtabs %}
