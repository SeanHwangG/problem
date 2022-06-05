# [HR_average-population](https://www.hackerrank.com/challenges/average-population)

```en
Query the average population for all cities in CITY, rounded down to the nearest integer
```

```txt
Input: 
| Population | City       | Country | State        | Zip    |
| ---------- | ---------- | ------- | ------------ | ------ |
| 100        | Rotterdam  | JPN     | Zuid-Holland | 593321 |
| 200        | Ecottsdale | USA     | Arizona      | 202705 |
| 300        | Corona     | USA     | California   | 124966 |

Output:

| Poplution |
| --------- |
| 400       |
```

## Solution

* sql

  ```sql
  SELECT ROUND(AVG(Population)) FROM City;
  ```
