# [LC_customers-who-never-order](https://leetcode.com/problems/customers-who-never-order)

Find all customers who never order anything


```txt
Input: 
| Id  | Name  |
| --- | ----- |
| 1   | Joe   |
| 2   | Henry |
| 3   | Sam   |
| 4   | Max   |

| Id  | CustomerId |
| --- | ---------- |
| 1   | 3          |
| 2   | 1          |

Output:

| Customers |
| --------- |
| Henry     |
| Max       |

```

## Solution

* sql

  ```sql
  SELECT A.Name from Customers A
    WHERE NOT EXISTS (SELECT 1 FROM Orders B WHERE A.Id = B.CustomerId limit 1)
  ```
