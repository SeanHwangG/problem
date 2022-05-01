# [LC_product-sales-analysis-iii](https://leetcode.com/problems/product-sales-analysis-iii)

Selects product id, year, quantity, and price for first year of every product sold

```txt
Input: 
| sale_id | product_id | year | quantity | price |
| ------- | ---------- | ---- | -------- | ----- |
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |

| product_id | product_name |
| ---------- | ------------ |
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |

Output:
| product_id | first_year | quantity | price |
| ---------- | ---------- | -------- | ----- |
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |
```

## Solution

* sql

  ```sql
  SELECT s2.product_id, s2.year AS "first_year", s2.quantity, s2.price FROM Sales s2
    JOIN (SELECT s.product_id, MIN(s.year) AS "year" FROM Sales s
          GROUP BY s.product_id ) first_year
    ON s2.product_id = first_year.product_id AND s2.year = first_year.year
  ```
