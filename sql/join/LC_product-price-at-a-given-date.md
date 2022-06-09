# [LC_product-price-at-a-given-date](https://leetcode.com/problems/product-price-at-a-given-date)

* en

  ```en
  Find prices of all products on 2019-08-16, Assume price of all products before any change is 1
  ```

* tc

  ```tc
  Input:
  | product_id | new_price | change_date |
  | ---------- | --------- | ----------- |
  | 1          | 20        | 2019-08-14  |
  | 2          | 50        | 2019-08-14  |
  | 1          | 30        | 2019-08-15  |
  | 1          | 35        | 2019-08-16  |
  | 2          | 65        | 2019-08-17  |
  | 3          | 20        | 2019-08-18  |

  Output:
  | product_id | price |
  | ---------- | ----- |
  | 2          | 50    |
  | 1          | 35    |
  | 3          | 10    |
  ```

## Solution

* sql

  ```sql
  SELECT distinct a.product_id, ifnull(temp.new_price, 10) as price FROM products as a LEFT JOIN
  (SELECT * FROM products WHERE (product_id, change_date) in
    (select product_id, max(change_date) from products where change_date <= "2019-08-16" group by product_id)) as temp
  on a.product_id = temp.product_id;
  ```
