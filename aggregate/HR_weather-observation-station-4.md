# [HR_weather-observation-station-4](https://www.hackerrank.com/challenges/weather-observation-station-4)

Find difference between total number of CITY entries in table and number of distinct CITY entries in table

```txt
Input: 
| Id   | City       | Country | State        | Zip    |
| ---- | ---------- | ------- | ------------ | ------ |
| 6    | Rotterdam  | NLD     | Zuid-Holland | 593321 |
| 1661 | Ecottsdale | USA     | Arizona      | 202705 |
| 3965 | Corona     | USA     | California   | 124966 |

Output:
| Count |
| ----- |
| 13    |
```

## Solution

```sql
SELECT COUNT(City) - COUNT(DISTINCT City) FROM Station;
```
