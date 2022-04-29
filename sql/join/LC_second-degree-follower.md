# [LC_second-degree-follower](https://leetcode.com/problems/second-degree-follower)

Get amount of each follower’s follower if he/she has one

```txt
Input:
| followee | follower |
| -------- | -------- |
| A        | B        |
| B        | C        |
| B        | D        |
| D        | E        |

Output:
| follower | num |
| -------- | --- |
| B        | 2   |
| D        | 1   |
```

## Solution

```sql
SELECT DISTINCT f.follower, f3.num FROM follow f
  JOIN (SELECT f2.followee, COUNT(DISTINCT f2.follower) AS "num"
        FROM follow f2 GROUP BY f2.followee) f3
  ON f.follower = f3.followee ORDER BY f.follower
```
