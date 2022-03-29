```sql
WITH order_table AS (
  SELECT *,
    ROW_NUMBER() OVER(PARTITION BY u.username ORDER BY u.startDate DESC) AS 'order',
    COUNT(1) OVER(PARTITION BY u.username) AS 'act_count' FROM UserActivity u)
SELECT o.username, o.activity, o.startDate, o.endDate FROM order_table o
  WHERE o.order = 2 OR o.act_count = 1
```
