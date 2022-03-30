# [LC_winning-candidate](https://leetcode.com/problems/winning-candidate)

Find the name of the winning candidate, the above example will return the winner B

```txt
Input:
Candidate
  | id  | Name |
  | --- | ---- |
  | 1   | A    |
  | 2   | B    |
  | 3   | C    |
  | 4   | D    |
  | 5   | E    |

Vote
  | id  | CandidateId |
  | --- | ----------- |
  | 1   | 2           |
  | 2   | 4           |
  | 3   | 3           |
  | 4   | 2           |
  | 5   | 5           |

Output:
| Name |
| ---- |
| B    |
```

## Solution

```sql
SELECT Name
FROM Candidate
WHERE id = (SELECT CandidateId
  FROM Vote
  GROUP BY CandidateId
  ORDER BY COUNT(*) DESC
  LIMIT 1);
```
