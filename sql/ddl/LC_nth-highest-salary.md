# [LC_nth-highest-salary](https://leetcode.com/problems/nth-highest-salary)

```en
Get nth highest salary from Employee table
```

```txt
Input: 
| Id  | Salary |
| --- | ------ |
| 1   | 100    |
| 2   | 200    |
| 3   | 300    |

Output:
| getNthHighestSalary(2) |
| ---------------------- |
| 200                    |
```

## Solution

* sql

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
