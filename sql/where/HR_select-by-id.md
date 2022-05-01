# [HR_select-by-id](https://www.hackerrank.com/challenges/select-by-id)

All columns for a city in CITY with the ID 1661

```txt
Input:
| Id   | City       | Country | State        | Zip    |
| ---- | ---------- | ------- | ------------ | ------ |
| 6    | Rotterdam  | NLD     | Zuid-Holland | 593321 |
| 1661 | Ecottsdale | USA     | Arizona      | 202705 |
| 3965 | Corona     | USA     | California   | 124966 |

Input:
| Id   | City       | Country | State   | Zip    |
| ---- | ---------- | ------- | ------- | ------ |
| 1661 | Ecottsdale | USA     | Arizona | 202705 |
```

## Solution

* sql

  ```sql
  SELECT * FROM City WHERE Id = 1661;
  ```
