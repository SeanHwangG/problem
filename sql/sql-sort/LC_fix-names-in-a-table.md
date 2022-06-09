# [LC_fix-names-in-a-table](https://leetcode.com/problems/fix-names-in-a-table)

* en

  ```en
  Fix names so that only first character is uppercase and rest are lowercase
  Return result table ordered by user_id
  ```

* tc

  ```tc
  Input:
  | user_id | name  |
  | ------- | ----- |
  | 1       | aLice |
  | 2       | bOB   |

  Output:
  | user_id | name  |
  | ------- | ----- |
  | 1       | Alice |
  | 2       | Bob   |
  ```

## Solution

* sql

  ```sql
  SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS 'name'
    FROM Users
    ORDER BY user_id ASC
  ```
