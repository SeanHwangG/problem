{% tabs %}{% tab title='HR_weather-observation-station-5.sql' %}

```sql
( SELECT City, LENGTH(City) FROM Station
  ORDER BY LENGTH(City) ASC, City LIMIT 1) UNION
( SELECT City, LENGTH(City) FROM Station
  ORDER BY LENGTH(City) DESC, City LIMIT 1);
```

{% endtab %}{% endtabs %}
