# [LC_reported-posts-ii](https://leetcode.com/problems/reported-posts-ii)

* en

  ```en
  Find average for daily percentage of posts that got removed after being reported as spam, rounded to 2 decimal places
  2019-07-04 is 50% / 2019-07-02 is 100%
  ```

* tc

  ```tc
  Input:
  | user_id | post_id | action_date | action | extra  |
  | ------- | ------- | ----------- | ------ | ------ |
  | 1       | 1       | 2019-07-01  | view   | null   |
  | 1       | 1       | 2019-07-01  | like   | null   |
  | 1       | 1       | 2019-07-01  | share  | null   |
  | 2       | 2       | 2019-07-04  | view   | null   |
  | 2       | 2       | 2019-07-04  | report | spam   |
  | 3       | 4       | 2019-07-04  | view   | null   |
  | 3       | 4       | 2019-07-04  | report | spam   |
  | 4       | 3       | 2019-07-02  | view   | null   |
  | 4       | 3       | 2019-07-02  | report | spam   |
  | 5       | 2       | 2019-07-03  | view   | null   |
  | 5       | 2       | 2019-07-03  | report | racism |
  | 5       | 5       | 2019-07-03  | view   | null   |
  | 5       | 5       | 2019-07-03  | report | racism |

  | post_id | remove_date |
  | ------- | ----------- |
  | 2       | 2019-07-20  |
  | 3       | 2019-07-18  |

  Output:
  | average_daily_percent |
  | --------------------- |
  | 75.00                 |
  ```

## Solution

* sql

  ```sql
  SELECT ROUND(100*AVG(Ratio),2) AS 'average_daily_percent' FROM
    (SELECT A.action_date, COUNT(R.remove_date)/COUNT(*) AS Ratio FROM
      (SElECT DISTINCT post_id,action_date FROM Actions
        WHERE action='report' and extra='spam') AS A
        LEFT JOIN Removals R ON A.post_id = R.post_id GROUP BY A.action_date) AS B
  ```
