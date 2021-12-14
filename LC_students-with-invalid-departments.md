{% tabs %}{% tab title='LC_1350.sql' %}

```sql
SELECT s.id, s.name FROM Students s
  LEFT JOIN Departments d on s.department_id = d.id
  WHERE d.name is null
```

{% endtab %}{% endtabs %}
