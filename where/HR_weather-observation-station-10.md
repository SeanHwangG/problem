```sql
SELECT DISTINCT City FROM Station
  WHERE RIGHT(City, 1) NOT IN ('A', 'E', 'I', 'O', 'U');
```
