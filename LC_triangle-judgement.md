{% tabs %}{% tab title='LC_610.md' %}

| x   | y   | z   |
| --- | --- | --- |
| 13  | 15  | 30  |
| 10  | 20  | 15  |

* judge whether these three sides can form a triangle

| x   | y   | z   | triangle |
| --- | --- | --- | -------- |
| 13  | 15  | 30  | No       |
| 10  | 20  | 15  | Yes      |

{% endtab %}{% tab title='LC_610.py' %}

```sql
SELECT x, y, z,
  CASE WHEN x+y<=z OR x+z<=y OR y+z<=x THEN 'No' ELSE 'Yes' END
  AS 'triangle' FROM triangle;
```

{% endtab %}{% endtabs %}
