{% tabs %}{% tab title='LC_612.py' %}

```sql
SELECT ROUND(MIN(SQRT(pow(p1.x-p2.x,2)+pow(p1.y-p2.y,2))),2) AS 'shortest'
  FROM point_2d p1, point_2d p2 WHERE not (p1.x = p2.x and p1.y = p2.y)
```

{% endtab %}{% endtabs %}
