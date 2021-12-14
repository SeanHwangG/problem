{% tabs %}{% tab title='LC_595.sql' %}

```sql
SELECT name, population, area FROM World
  WHERE 3000000 < area OR 25000000 < population;
```

{% endtab %}{% endtabs %}
