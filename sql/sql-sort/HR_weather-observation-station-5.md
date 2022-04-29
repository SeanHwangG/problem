# [HR_weather-observation-station-5](https://www.hackerrank.com/challenges/weather-observation-station-5)

Query two cities in STATION with the shortest and longest CITY names, as well as their respective lengths
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically

```txt
Input: 

  | Id   | City       | Country | State        | Zip    |
  | ---- | ---------- | ------- | ------------ | ------ |
  | 6    | Rotterdam  | JPN     | Zuid-Holland | 593321 |
  | 1661 | Ecottsdale | USA     | Arizona      | 202705 |
  | 3965 | Corona     | USA     | California   | 124966 |

Output:

  | City       | Length |
  | ---------- | ------ |
  | Corona     | 6      |
  | Ecottsdale | 10     |

```

## Solution

```sql
( SELECT City, LENGTH(City) FROM Station
  ORDER BY LENGTH(City) ASC, City LIMIT 1) UNION
( SELECT City, LENGTH(City) FROM Station
  ORDER BY LENGTH(City) DESC, City LIMIT 1);
```
