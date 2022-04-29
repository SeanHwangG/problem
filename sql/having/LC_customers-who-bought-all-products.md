# [LC_customers-who-bought-all-products](https://leetcode.com/problems/customers-who-bought-all-products)

Report that provides the customer ids from the Customer table that bought all the products in the Product table

```txt
Input:
* Customer

| customer_id | product_key |
| ----------- | ----------- |
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |

* Product

| product_key |
| ----------- |
| 5           |
| 6           |

Output:
| customer_id |
| ----------- |
| 1           |
| 3           |
```

## Solution

```sql
SELECT customer_id FROM (SELECT * FROM Customer WHERE product_key in (SELECT * FROM Product)) AS A
  GROUP BY customer_id
  HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(product_key) FROM Product)
```
