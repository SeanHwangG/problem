# [LC_triangle-judgement](https://leetcode.com/problems/triangle-judgement)

* en

  ```en
  Judge whether these three sides can form a triangle
  ```

* tc

  ```tc
  Input:
  | x   | y   | z   |
  | --- | --- | --- |
  | 13  | 15  | 30  |
  | 10  | 20  | 15  |

  Output:
  | x   | y   | z   | triangle |
  | --- | --- | --- | -------- |
  | 13  | 15  | 30  | No       |
  | 10  | 20  | 15  | Yes      |
  ```

## Solution

* sql

  ```sql
  SELECT x, y, z,
    CASE WHEN x+y<=z OR x+z<=y OR y+z<=x THEN 'No' ELSE 'Yes' END
    AS 'triangle' FROM triangle;
  ```
