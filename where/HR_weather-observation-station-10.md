# [HR_weather-observation-station-10](https://www.hackerrank.com/challenges/weather-observation-station-10)

List of CITY names from STATION that do not end with vowels without duplicates

```txt
Input:
| Id   | City       | Country | State        | Zip    |
| ---- | ---------- | ------- | ------------ | ------ |
| 6    | Rotterdam  | NLD     | Zuid-Holland | 593321 |
| 1661 | Ecottsdale | USA     | Arizona      | 202705 |
| 3965 | Corona     | USA     | California   | 124966 |

Output:
| Id  | City      | Country | State        | Zip    |
| --- | --------- | ------- | ------------ | ------ |
| 6   | Rotterdam | NLD     | Zuid-Holland | 593321 |
```

## Solution

```sql
SELECT DISTINCT City FROM Station
  WHERE RIGHT(City, 1) NOT IN ('A', 'E', 'I', 'O', 'U');
```
