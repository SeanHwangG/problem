# [LC_swap-salary](https://leetcode.com/problems/swap-salary)

swap all 'f' and 'm' values with a single update statement and no intermediate temp table


```txt
Input: 
| id  | name | sex | salary |
| --- | ---- | --- | ------ |
| 1   | A    | m   | 2500   |
| 2   | B    | f   | 1500   |
| 3   | C    | m   | 5500   |
| 4   | D    | f   | 500    |

Output:
| id  | name | sex | salary |
| --- | ---- | --- | ------ |
| 1   | A    | f   | 2500   |
| 2   | B    | m   | 1500   |
| 3   | C    | f   | 5500   |
| 4   | D    | m   | 500    |
```

## Solution

* sql

  ```sql
  UPDATE salary SET sex =
    CASE sex
      WHEN 'f' THEN 'm'
      WHEN 'm' THEN 'f'
    END
  ```
