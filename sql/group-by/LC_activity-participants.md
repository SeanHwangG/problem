# [LC_activity-participants](https://leetcode.com/problems/activity-participants)

```en
Find names of all activities with neither max, nor min number of participants in any order
Each activity in table Activities is performed by any person in table Friends
```

```txt
Input: 
| id  | name        | activity     |
| --- | ----------- | ------------ |
| 1   | Jonathan D. | Eating       |
| 2   | Jade W.     | Singing      |
| 3   | Victor J.   | Singing      |
| 4   | Elvis Q.    | Eating       |
| 5   | Daniel A.   | Eating       |
| 6   | Bob B.      | Horse Riding |

| id  | name         |
| --- | ------------ |
| 1   | Eating       |
| 2   | Singing      |
| 3   | Horse Riding |

Output:
| results |
| ------- |
| Singing |
```

## Solution

* sql

  ```sql
  WITH activity_count AS (
      SELECT f.activity, COUNT(1) AS 'act_counts' FROM Friends f
      GROUP BY f.activity)

  SELECT a.activity FROM activity_count a
    WHERE a.act_counts != (SELECT MAX(act_counts) FROM activity_count)
    AND a.act_counts != (SELECT MIN(act_counts) FROM activity_count)
  ```
