# [HR_weather-observation-station-16](https://www.hackerrank.com/challenges/weather-observation-station-16)

Smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7780
Round your answer to 4 decimal places

```txt
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

```sql
SELECT TRUNCATE(SUM(LAT_N), 4) FROM Station
  WHERE LAT_N > 38.7880 AND LAT_N < 137.2345;
```
