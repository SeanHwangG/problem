# [HR_the-blunder](https://www.hackerrank.com/challenges/the-blunder)

```en
Finding difference between miscalculation (salaries with any zeros removed), and actual average salary
```

```txt
Input:
| ID  | Name     | Salary |
| --- | -------- | ------ |
| 1   | Kristeen | 1420   |
| 2   | Ashley   | 2006   |
| 3   | Julia    | 2210   |
| 4   | Maria    | 3000   |

Output:
| Salary |
| ------ |
| 2061   |
```

## Solution

* sql

  ```sql
  SELECT CEIL(AVG(Salary) - AVG(REPLACE(CAST(Salary AS CHAR), "0", ""))) FROM Employees;
  ```
