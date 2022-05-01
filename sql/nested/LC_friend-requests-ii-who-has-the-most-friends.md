# [LC_friend-requests-ii-who-has-the-most-friends](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends)

Find the people who has most friends and the most friends number

```txt
Input: 
| requester_id | accepter_id | accept_date |
| ------------ | ----------- | ----------- |
| 1            | 2           | 2016_06-03  |
| 1            | 3           | 2016-06-08  |
| 2            | 3           | 2016-06-08  |
| 3            | 4           | 2016-06-09  |

Output:
| id  | num |
| --- | --- |
| 3   | 3   |
```

## Solution

* sql

  ```sql
  SELECT union_table.requester_id AS "id", COUNT(*) AS "num"
    FROM (SELECT r.requester_id FROM request_accepted r
          UNION ALL (SELECT r2.accepter_id FROM request_accepted r2)) union_table
    GROUP BY union_table.requester_id
    ORDER BY num DESC LIMIT 1
  ```
