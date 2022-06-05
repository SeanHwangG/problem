# [LC_shortest-distance-in-a-plane](https://leetcode.com/problems/shortest-distance-in-a-plane)

```en
Find the shortest distance between these points rounded to 2 decimals
The shortest distance is 1.00 from point (-1,-1) to (-1,2)
```

```txt
Input: 
| x   | y   |
| --- | --- |
| -1  | -1  |
| 0   | 0   |
| -1  | -2  |

Output:
| shortest |
| -------- |
| 1.00     |
```

## Solution

* sql

  ```sql
  SELECT ROUND(MIN(SQRT(pow(p1.x-p2.x,2)+pow(p1.y-p2.y,2))),2) AS 'shortest'
    FROM point_2d p1, point_2d p2 WHERE not (p1.x = p2.x and p1.y = p2.y)
  ```
