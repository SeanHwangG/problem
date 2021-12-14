{% tabs %}{% tab title='HR_weather-observation-station-10.sql' %}

```sql
SELECT DISTINCT City FROM Station
  WHERE RIGHT(City, 1) NOT IN ('A', 'E', 'I', 'O', 'U');
```

{% endtab %}{% endtabs %}
