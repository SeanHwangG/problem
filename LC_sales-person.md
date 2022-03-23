```sql
SELECT salesperson.name FROM orders o
  JOIN company c ON (o.com_id = c.com_id AND c.name = 'RED')
  RIGHT JOIN salesperson ON Salesperson.sales_id = o.sales_id
  WHERE o.sales_id IS Null
```
