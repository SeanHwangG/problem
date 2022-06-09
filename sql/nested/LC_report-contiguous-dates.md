# [LC_report-contiguous-dates](https://leetcode.com/problems/report-contiguous-dates)

* en

  ```en
  Generate a report of period_state for each continuous interval of days in period from 2019-01-01 to 2019-12-31
  ```

* tc

  ```tc
  Input:
  | fail_date  |
  | ---------- |
  | 2018-12-28 |
  | 2018-12-29 |
  | 2019-01-04 |
  | 2019-01-05 |

  | success_date |
  | ------------ |
  | 2018-12-30   |
  | 2018-12-31   |
  | 2019-01-01   |
  | 2019-01-02   |
  | 2019-01-03   |
  | 2019-01-06   |

  Output:

  | period_state | start_date | end_date   |
  | ------------ | ---------- | ---------- |
  | succeeded    | 2019-01-01 | 2019-01-03 |
  | failed       | 2019-01-04 | 2019-01-05 |
  | succeeded    | 2019-01-06 | 2019-01-06 |
  ```

## Solution

* sql

  ```sql
  SELECT stats AS period_state, MIN(day) AS start_date, MAX(day) AS end_date
  FROM (
    SELECT day, RANK() OVER (ORDER BY day) AS overall_ranking, stats, rk,
      (RANK() OVER (ORDER BY day) - rk) AS inv
    FROM (
      SELECT fail_date AS day, 'failed' AS stats, RANK() OVER (ORDER BY fail_date) AS rk
      FROM Failed WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
      UNION
      SELECT success_date AS day, 'succeeded' AS stats, RANK() OVER (ORDER BY success_date) AS rk
      FROM Succeeded WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31') t
    ) c
  GROUP BY inv, stats
  ORDER BY start_date
  ```
