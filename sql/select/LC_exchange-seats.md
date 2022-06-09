# [LC_exchange-seats](https://leetcode.com/problems/exchange-seats)

* en

  ```en
  Mary is teacher in middle school and she has a table seat storing students' names and their corresponding seat ids
  The column id is continuous increment
  Change seats for the adjacent students
  ```

* tc

  ```tc
  Input:
    | id  | student |
    | --- | ------- |
    | 1   | Abbot   |
    | 2   | Doris   |
    | 3   | Emerson |
    | 4   | Green   |
    | 5   | Jeames  |

  Ouput:
    | id  | student |
    | --- | ------- |
    | 1   | Doris   |
    | 2   | Abbot   |
    | 3   | Green   |
    | 4   | Emerson |
    | 5   | Jeames  |
  ```

## Solution

* sql

  ```sql
  SELECT
    IF(id < (SELECT count(*) from seat), IF(id MOD 2=0, id-1, id+1), IF(id MOD 2=0, id-1, id)) as id, student
  FROM seat ORDER BY id asc;
  ```
