# [HR_weather-observation-station-13](https://www.hackerrank.com/challenges/weather-observation-station-13)

* en

  ```en
  Sum of Northern Latitudes (LAT_N) from STATION having values greater than 38.7880 and less than 137.2345
  Truncate your answer to 4 decimal places
  ```

* tc

  ```tc
  Input:
  | LAT_N | City       |
  | ----- | ---------- |
  | 10    | Rotterdam  |
  | 123   | Ecottsdale |
  | 300   | Corona     |

  Output:
  | SUM      |
  | -------- |
  | 123.0000 |
  ```

## Solution

* sql

  ```sql
  SELECT TRUNCATE(SUM(LAT_N), 4) FROM Station
    WHERE LAT_N > 38.7880 AND LAT_N < 137.2345;
  ```
