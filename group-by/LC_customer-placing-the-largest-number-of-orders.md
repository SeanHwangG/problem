# [LC_customer-placing-the-largest-number-of-orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders)

Find customer_number for the customer who has placed the largest number of orders

```txt
Input:
| order_number | customer_number |
|--------------|-----------------|
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |

Output:
| customer_number |
|-----------------|
| 3               |
```

## Solution

```sql
SELECT  customer_number FROM orders
  GROUP BY customer_number
  ORDER BY COUNT(order_number) DESC LIMIT 1
```
