# [HR_what-type-of-triangle](https://www.hackerrank.com/challenges/what-type-of-triangle)

* en

  ```en
  Determine type of each triangle
  ```

* tc

  ```tc
  Input:
  | A   | B   | C   |
  | --- | --- | --- |
  | 20  | 20  | 23  |
  | 20  | 20  | 20  |
  | 20  | 21  | 22  |
  | 13  | 14  | 30  |

  Output:
  | Type           |
  | -------------- |
  | Isosceles      |
  | Equilateral    |
  | Scalene        |
  | Not A Triangle |
  ```

## Solution

* sql

  ```sql
  SELECT CASE WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
              WHEN A = B AND B = C THEN 'Equilateral'
              WHEN A = B OR A = C OR B = C THEN 'Isosceles'
              ELSE 'Scalene'
    END
  FROM TRIANGLES
  ```
