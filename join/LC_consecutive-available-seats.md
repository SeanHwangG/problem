# [LC_consecutive-available-seats](https://leetcode.com/problems/consecutive-available-seats)

Query all consecutive available seats order by the seat_id

```txt
Input:

| seat_id | free |
| ------- | ---- |
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |

Output:

| seat_id |
| ------- |
| 3       |
| 4       |
| 5       |
```

## Solution

```sql
SELECT DISTINCT a.seat_id FROM cinema a
  JOIN cinema b ON abs(a.seat_id - b.seat_id) = 1 AND a.free=true AND b.free=true
  ORDER BY a.seat_id;
```
