# [HR_weather-observation-station-1](https://www.hackerrank.com/challenges/weather-observation-station-1)

Query a list of CITY and STATE from the STATION table

```txt
Input:
* Station

| Field  | Type     |
| ------ | -------- |
| ID     | NUMBER   |
| CITY   | VARCHAR2 |
| STATE  | VARCHAR2 |
| LAT_N  | NUMBER   |
| LONG_W | NUMBER   |

Output:
| City    | State |
| ------- | ----- |
| Acme    | LA    |
| Addison | MI    |
| Agency  | MO    |
| Aguanga | CA    |
| Alanson | MI    |
```

## Solution

* sql

  ```sql
  SELECT City, State FROM STATION;
  ```
