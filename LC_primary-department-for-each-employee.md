{% tabs %}{% tab title='LC_1789.sql' %}

```sql
SELECT e.employee_id , e.department_id FROM Employee e
  WHERE e.primary_flag = 'Y'
  UNION (
    SELECT e2.employee_id , e2.department_id FROM Employee e2
    GROUP BY e2.employee_id HAVING COUNT(1) = 1
  )
```

{% endtab %}{% endtabs %}
