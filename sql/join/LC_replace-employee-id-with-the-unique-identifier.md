# [LC_replace-employee-id-with-the-unique-identifier](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier)

```en
Show the unique ID of each user, If a user doesn't have a unique ID replace just show null
```

```txt
Input:

| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |

| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |

Output:

| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
```

## Solution

* sql

  ```sql
  SELECT eu.unique_id, e.name FROM EmployeeUNI eu
    RIGHT JOIN Employees e ON eu.id= e.id;
  ```
