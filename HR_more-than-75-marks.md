{% tabs %}{% tab title='HR_more-than-75-marks.sql' %}

```sql
SELECT Name FROM Students WHERE Marks > 75
  ORDER BY RIGHT(Name, 3), Id;
```

{% endtab %}{% endtabs %}
