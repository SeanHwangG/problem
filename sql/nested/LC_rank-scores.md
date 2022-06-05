# [LC_rank-scores](https://leetcode.com/problems/rank-scores)

```en
Rank scores if there is a tie between two scores, both should have the same ranking
```

```txt
Input:
| Id  | Score |
| --- | ----- |
| 1   | 3.50  |
| 2   | 3.65  |
| 3   | 4.00  |
| 4   | 3.85  |
| 5   | 4.00  |
| 6   | 3.65  |

Output:
| score | Rank |
| ----- | ---- |
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
```

## Solution

* sql

  ```sql
  SELECT S.Score, COUNT(S2.Score) as `Rank` FROM Scores S, (SELECT DISTINCT Score FROM Scores) S2
    WHERE S.Score <= S2.Score GROUP BY S.Id ORDER BY S.Score DESC;
  ```
