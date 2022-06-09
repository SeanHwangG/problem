# [LC_second-highest-salary](https://leetcode.com/problems/second-highest-salary)

* en

  ```en
  Find second highest salary from the Employee table
  ```

* tc

  ```tc
  Input:
  | Id  | Salary |
  | --- | ------ |
  | 1   | 100    |
  | 2   | 200    |
  | 3   | 300    |

  Output:
  | SecondHighestSalary |
  | ------------------- |
  | 200                 |
  ```

## Solution

* sql

  ```sql
  SELECT MAX(Salary) SecondHighestSalary FROM Employee
    WHERE Salary != (SELECT MAX(Salary) FROM Employee);
  ```
