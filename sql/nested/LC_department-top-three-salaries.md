# [LC_department-top-three-salaries](https://leetcode.com/problems/department-top-three-salaries)

```en
Find employees who earn the top three salaries in each of the department

```

```txt
Input: 

* Employee

  | Id  | Name  | Salary | DepartmentId |
  | --- | ----- | ------ | ------------ |
  | 1   | Joe   | 85000  | 1            |
  | 2   | Henry | 80000  | 2            |
  | 3   | Sam   | 60000  | 2            |
  | 4   | Max   | 90000  | 1            |
  | 5   | Janet | 69000  | 1            |
  | 6   | Randy | 85000  | 1            |
  | 7   | Will  | 70000  | 1            |

* Department

  | Id  | Name  |
  | --- | ----- |
  | 1   | IT    |
  | 2   | Sales |

Output:
| Department | Employee | Salary |
| ---------- | -------- | ------ |
| IT         | Max      | 90000  |
| IT         | Randy    | 85000  |
| IT         | Joe      | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
```

## Solution

* sql

  ```sql
  SELECT dep.Name Department, emp.Name Employee, emp.Salary FROM Department dep, Employee emp
    WHERE emp.DepartmentId=dep.Id AND
    (SELECT count(DISTINCT Salary) FROM Employee WHERE DepartmentId=dep.Id AND Salary>emp.Salary) < 3
  ```
