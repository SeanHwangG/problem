{% tabs %}{% tab title='HR_the-blunder.sql' %}

```sql
SELECT CEIL(AVG(Salary) - AVG(REPLACE(CAST(Salary AS CHAR), "0", ""))) FROM Employees;
```

{% endtab %}{% endtabs %}
