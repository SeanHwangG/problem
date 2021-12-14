{% tabs %}{% tab title='LC_176.sql' %}

```sql
SELECT MAX(Salary) SecondHighestSalary FROM Employee
  WHERE Salary != (SELECT MAX(Salary) FROM Employee);
```

{% endtab %}{% endtabs %}
