{% tabs %}{% tab title='LC_177.md' %}

| Id  | Salary |
| --- | ------ |
| 1   | 100    |
| 2   | 200    |
| 3   | 300    |

* Write a SQL query to get the nth highest salary from the Employee table

| getNthHighestSalary(2) |
| ---------------------- |
| 200                    |

{% endtab %}{% tab title='LC_177.sql' %}

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1;
  RETURN (
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT M, 1
  );
END
```

{% endtab %}{% endtabs %}
