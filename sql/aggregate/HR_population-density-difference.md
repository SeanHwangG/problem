# [HR_population-density-difference](https://www.hackerrank.com/challenges/population-density-difference)

* en

  ```en
  Query the difference between the maximum and minimum populations in CITY
  ```

* tc

  ```tc
  Input:
  | Population | City       | Country | State        | Zip    |
  | ---------- | ---------- | ------- | ------------ | ------ |
  | 100        | Rotterdam  | JPN     | Zuid-Holland | 593321 |
  | 200        | Ecottsdale | USA     | Arizona      | 202705 |
  | 300        | Corona     | USA     | California   | 124966 |

  Output:
  | Poplution |
  | --------- |
  | 200       |
  ```

## Solution

* sql

  ```sql
  SELECT MAX(Population) - MIN(Population) FROM City;
  ```
