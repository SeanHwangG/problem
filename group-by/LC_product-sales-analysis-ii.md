```sql
SELECT s.product_id, SUM(s.quantity) AS "total_quantity" FROM Sales s
  GROUP BY s.product_id
```
