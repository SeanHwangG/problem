# [LC_count-apples-and-oranges](https://leetcode.com/problems/count-apples-and-oranges)

Report difference between number of apples and oranges sold each day
Return result table ordered by sale_date in format ('YYYY-MM-DD')

```txt
Input:
Sales
  | sale_date  | fruit   | sold_num |
  | ---------- | ------- | -------- |
  | 2020-05-01 | apples  | 10       |
  | 2020-05-01 | oranges | 8        |
  | 2020-05-02 | apples  | 15       |
  | 2020-05-02 | oranges | 15       |
  | 2020-05-03 | apples  | 20       |
  | 2020-05-03 | oranges | 0        |
  | 2020-05-04 | apples  | 15       |
  | 2020-05-04 | oranges | 16       |

Output:
| sale_date  | diff |
| ---------- | ---- |
| 2020-05-01 | 2    |
| 2020-05-02 | 0    |
| 2020-05-03 | 20   |
| 2020-05-04 | -1   |
```

## Solution

```sql
SELECT sale_date, sum(CASE WHEN fruit='apples' THEN sold_num ELSE -sold_num END) AS diff FROM Sales
  GROUP BY sale_date
```
