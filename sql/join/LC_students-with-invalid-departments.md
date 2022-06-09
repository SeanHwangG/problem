# [LC_students-with-invalid-departments](https://leetcode.com/problems/students-with-invalid-departments)

* en

  ```en
  Find id and name of all students who are enrolled in departments that no longer exists in any order
  ```

* tc

  ```tc
  Input:

  | id  | name                     |
  | --- | ------------------------ |
  | 1   | Electrical Engineering   |
  | 7   | Computer Engineering     |
  | 13  | Bussiness Administration |

  | id  | name     | department_id |
  | --- | -------- | ------------- |
  | 23  | Alice    | 1             |
  | 1   | Bob      | 7             |
  | 5   | Jennifer | 13            |
  | 2   | John     | 14            |
  | 4   | Jasmine  | 77            |
  | 3   | Steve    | 74            |
  | 6   | Luis     | 1             |
  | 8   | Jonathan | 7             |
  | 7   | Daiana   | 33            |
  | 11  | Madelynn | 1             |

  Output:

  | id  | name    |
  | --- | ------- |
  | 2   | John    |
  | 7   | Daiana  |
  | 4   | Jasmine |
  | 3   | Steve   |
  ```

## Solution

* sql

  ```sql
  SELECT s.id, s.name FROM Students s
    LEFT JOIN Departments d on s.department_id = d.id
    WHERE d.name is null
  ```
