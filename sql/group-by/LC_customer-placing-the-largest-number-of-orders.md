# [LC_customer-placing-the-largest-number-of-orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders)

* en

  ```en
  Find customer_number for the customer who has placed the largest number of orders
  ```

* tc

  ```tc
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

* sql

  ```sql
  SELECT  customer_number FROM orders
    GROUP BY customer_number
    ORDER BY COUNT(order_number) DESC LIMIT 1
  ```
