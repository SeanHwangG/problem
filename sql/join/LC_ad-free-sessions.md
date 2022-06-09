# [LC_ad-free-sessions](https://leetcode.com/problems/ad-free-sessions)

* en

  ```en
  Report all the sessions that did not get shown any ads in any order
  ```

* tc

  ```tc
  Input:

  | session_id | customer_id | start_time | end_time |
  | ---------- | ----------- | ---------- | -------- |
  | 1          | 1           | 1          | 5        |
  | 2          | 1           | 15         | 23       |
  | 3          | 2           | 10         | 12       |
  | 4          | 2           | 17         | 28       |
  | 5          | 2           | 2          | 8        |

  | ad_id | customer_id | timestamp |
  | ----- | ----------- | --------- |
  | 1     | 1           | 5         |
  | 2     | 2           | 15        |
  | 3     | 2           | 20        |

  Output:

  | session_id |
  | ---------- |
  | 2          |
  | 3          |
  | 5          |
  ```

## Solution

* sql

  ```sql
  SELECT p.session_id FROM Playback p
    LEFT JOIN Ads a ON a.timestamp BETWEEN p.start_time AND p.end_time AND p.customer_id = a.customer_id
    WHERE a.ad_id IS NULL
  ```
