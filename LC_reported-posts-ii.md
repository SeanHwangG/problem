```sql
SELECT ROUND(100*AVG(Ratio),2) AS 'average_daily_percent' FROM
  (SELECT A.action_date, COUNT(R.remove_date)/COUNT(*) AS Ratio FROM
    (SElECT DISTINCT post_id,action_date FROM Actions
      WHERE action='report' and extra='spam') AS A
      LEFT JOIN Removals R ON A.post_id = R.post_id GROUP BY A.action_date) AS B
```
