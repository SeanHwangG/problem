# [LC_primary-department-for-each-employee](https://leetcode.com/problems/primary-department-for-each-employee)

* en

  ```en
  Employee joins other departments, they need to decide which department is their primary department
  Note that when an employee belongs to only one department, their primary column is 'N'
  Report all employees with their primary department
  ```

* tc

  ```tc
  Input:
  | employee_id | department_id | primary_flag |
  | ----------- | ------------- | ------------ |
  | 1           | 1             | N            |
  | 2           | 1             | Y            |
  | 2           | 2             | N            |
  | 3           | 3             | N            |
  | 4           | 2             | N            |
  | 4           | 3             | Y            |
  | 4           | 4             | N            |

  Output:
  | employee_id | department_id |
  | ----------- | ------------- |
  | 1           | 1             |
  | 2           | 1             |
  | 3           | 3             |
  | 4           | 3             |
  ```

## Solution

* sql

  ```sql
  SELECT e.employee_id , e.department_id FROM Employee e
    WHERE e.primary_flag = 'Y'
    UNION (
      SELECT e2.employee_id , e2.department_id FROM Employee e2
      GROUP BY e2.employee_id HAVING COUNT(1) = 1
    )
  ```
