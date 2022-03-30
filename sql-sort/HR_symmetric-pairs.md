# [HR_symmetric-pairs](https://www.hackerrank.com/challenges/symmetric-pairs)

Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1
Output all such symmetric pairs in ascending order by the value of X. List the rows such that X1 ≤ Y1

```txt
Input:
| X   | Y   |
| --- | --- |
| 20  | 20  |
| 20  | 20  |
| 20  | 21  |
| 23  | 22  |
| 22  | 23  |
| 21  | 20  |

Output:
| X   | Y   |
| --- | --- |
| 20  | 20  |
| 20  | 21  |
| 22  | 23  |

```

## Solution

```sql
SELECT x, y FROM functions f1
  WHERE exists(SELECT * FROM functions f2 WHERE f2.y=f1.x
  AND f2.x=f1.y AND f2.x>f1.x) AND (x!=y) UNION
SELECT x, y FROM functions f1 WHERE x=y AND
  ((SELECT count(*) FROM functions WHERE x=f1.x AND y=f1.x) > 1) ORDER BY x;
```
