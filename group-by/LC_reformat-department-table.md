# [LC_reformat-department-table](https://leetcode.com/problems/reformat-department-table)

Reformat table such that there is a department id column and a revenue column for each month

```txt
Input:
| id  | revenue | month |
| --- | ------- | ----- |
| 1   | 8000    | Jan   |
| 2   | 9000    | Jan   |
| 3   | 10000   | Feb   |
| 1   | 7000    | Feb   |
| 1   | 6000    | Mar   |

Output:
| id  | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
| --- | ----------- | ----------- | ----------- | --- | ----------- |
| 1   | 8000        | 7000        | 6000        | ... | null        |
| 2   | 9000        | null        | null        | ... | null        |
| 3   | null        | 10000       | null        | ... | null        |
```

## Solution

```sql
SELECT id,
  SUM(CASE WHEN month="Jan" THEN revenue ELSE NULL END) as "Jan_Revenue",
  SUM(CASE WHEN month="Feb" THEN revenue ELSE NULL END) as "Feb_Revenue",
  SUM(CASE WHEN month="Mar" THEN revenue ELSE NULL END) as "Mar_Revenue",
  SUM(CASE WHEN month="Apr" THEN revenue ELSE NULL END) as "Apr_Revenue",
  SUM(CASE WHEN month="May" THEN revenue ELSE NULL END) as "May_Revenue",
  SUM(CASE WHEN month="Jun" THEN revenue ELSE NULL END) as "Jun_Revenue",
  AVG(CASE WHEN month="Jul" THEN revenue ELSE NULL END) as "Jul_Revenue",
  MAX(CASE WHEN month="Aug" THEN revenue ELSE NULL END) as "Aug_Revenue",
  SUM(CASE WHEN month="Sep" THEN revenue ELSE NULL END) as "Sep_Revenue",
  SUM(CASE WHEN month="Oct" THEN revenue ELSE NULL END) as "Oct_Revenue",
  SUM(CASE WHEN month="Nov" THEN revenue ELSE NULL END) as "Nov_Revenue",
  SUM(CASE WHEN month="Dec" THEN revenue ELSE NULL END) as "Dec_Revenue"
  FROM Department
  GROUP BY id
```
