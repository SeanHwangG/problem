# [HR_weather-observation-station-8](https://www.hackerrank.com/challenges/weather-observation-station-8)

```en
Query unique list of CITY names from STATION which have vowels as both their first and last characters
```

```txt
Input:
| Id   | City       | Country | State        | Zip    |
| ---- | ---------- | ------- | ------------ | ------ |
| 6    | Rotterdam  | JPN     | Zuid-Holland | 593321 |
| 1661 | Ecottsdale | USA     | Arizona      | 202705 |
| 3965 | Corona     | USA     | California   | 124966 |

Output:
| Id   | City       | Country | State   | Zip    |
| ---- | ---------- | ------- | ------- | ------ |
| 1661 | Ecottsdale | USA     | Arizona | 202705 |
```

## Solution

* sql

  ```sql
  SELECT DISTINCT city FROM station
    WHERE city REGEXP '^[aeiou].*[aeiou]$'
  ```
