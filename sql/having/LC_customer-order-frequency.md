# [LC_customer-order-frequency](https://leetcode.com/problems/customer-order-frequency)

```en
Report customer_id, customer_name of customers who have spent at least $100 in each month of June and July 2020
```

```txt
Input:
* Customers

  | customer_id  | name      | country     |
  +--------------+-----------+-------------+
  | 1            | Winston   | USA         |
  | 2            | Jonathan  | Peru        |
  | 3            | Moustafa  | Egypt       |

* Product

  | product_id   | description | price       |
  +--------------+-------------+-------------+
  | 10           | LC Phone    | 300         |
  | 20           | LC T-Shirt  | 10          |
  | 30           | LC Book     | 45          |
  | 40           | LC Keychain | 2           |

* Orders

  | order_id     | customer_id | product_id  | order_date  | quantity  |
  +--------------+-------------+-------------+-------------+-----------+
  | 1            | 1           | 10          | 2020-06-10  | 1         |
  | 2            | 1           | 20          | 2020-07-01  | 1         |
  | 3            | 1           | 30          | 2020-07-08  | 2         |
  | 4            | 2           | 10          | 2020-06-15  | 2         |
  | 5            | 2           | 40          | 2020-07-01  | 10        |
  | 6            | 3           | 20          | 2020-06-24  | 2         |
  | 7            | 3           | 30          | 2020-06-25  | 2         |
  | 9            | 3           | 30          | 2020-05-08  | 3         |

Output:

| customer_id  | name       |
+--------------+------------+
| 1            | Winston    |

```

## Solution

* sql

  ```sql
  SELECT customer_id, name FROM Customers
    JOIN Orders USING(customer_id) JOIN Product USING(product_id)
    GROUP BY customer_id
    HAVING SUM(IF(LEFT(order_date, 7) = '2020-06', quantity, 0) * price) >= 100
      AND SUM(IF(LEFT(order_date, 7) = '2020-07', quantity, 0) * price) >= 100
  ```
