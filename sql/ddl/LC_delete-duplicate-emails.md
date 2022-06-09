# [LC_delete-duplicate-emails](https://leetcode.com/problems/delete-duplicate-emails)

* en

  ```en
  Delete all duplicate email entries in table named Person, keeping only unique emails based on its smallest Id
  ```

* tc

  ```tc
  Input:
  | Id  | Email            |
  | --- | ---------------- |
  | 1   | john@example.com |
  | 2   | bob@example.com  |
  | 3   | john@example.com |

  Output:
  | Id  | Email            |
  | --- | ---------------- |
  | 1   | john@example.com |
  | 2   | bob@example.com  |
  ```

## Solution

* sql

  ```sql
  DELETE p1 FROM Person p1, Person p2 WHERE p2.Email = p1.Email AND p2.Id < p1.Id;
  ```
