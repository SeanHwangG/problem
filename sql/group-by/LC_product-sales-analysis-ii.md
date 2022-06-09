# [LC_product-sales-analysis-ii](https://leetcode.com/problems/product-sales-analysis-ii)

* en

  ```en
  Reports the total quantity sold for every product id
  ```

* tc

  ```tc
  Input:
  | sale_id | product_id | year | quantity | price |
  | ------- | ---------- | ---- | -------- | ----- |
  | 1       | 100        | 2008 | 10       | 5000  |
  | 2       | 100        | 2009 | 12       | 5000  |
  | 7       | 200        | 2011 | 15       | 9000  |

  Output:
  | product_id | total_quantity |
  | ---------- | -------------- |
  | 100        | 22             |
  | 200        | 15             |
  ```

## Solution

* sql

  ```sql
  SELECT s.product_id, SUM(s.quantity) AS "total_quantity" FROM Sales s
    GROUP BY s.product_id
  ```
