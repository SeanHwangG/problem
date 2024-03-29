# [LC_get-the-second-most-recent-activity](https://leetcode.com/problems/get-the-second-most-recent-activity)

* en

  ```en
  Show second most recent activity of each user
  If user only has one activity, return that one
  ```

* tc

  ```tc
  Input:
  | username | activity | startDate  | endDate    |
  | -------- | -------- | ---------- | ---------- |
  | Alice    | Travel   | 2020-02-12 | 2020-02-20 |
  | Alice    | Dancing  | 2020-02-21 | 2020-02-23 |
  | Alice    | Travel   | 2020-02-24 | 2020-02-28 |
  | Bob      | Travel   | 2020-02-11 | 2020-02-18 |

  Output:

  | username | activity | startDate  | endDate    |
  | -------- | -------- | ---------- | ---------- |
  | Alice    | Dancing  | 2020-02-21 | 2020-02-23 |
  | Bob      | Travel   | 2020-02-11 | 2020-02-18 |
  ```

## Solution

* sql

  ```sql
  WITH order_table AS (
    SELECT *,
      ROW_NUMBER() OVER(PARTITION BY u.username ORDER BY u.startDate DESC) AS 'order',
      COUNT(1) OVER(PARTITION BY u.username) AS 'act_count' FROM UserActivity u)
  SELECT o.username, o.activity, o.startDate, o.endDate FROM order_table o
    WHERE o.order = 2 OR o.act_count = 1
  ```
