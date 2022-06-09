# [LC_rising-temperature](https://leetcode.com/problems/rising-temperature)

* en

  ```en
  Find all id where temperature increased from previous date
  ```

* tc

  ```tc
  Input:
  | id  | recordDate | Temperature |
  | --- | ---------- | ----------- |
  | 1   | 2015-01-01 | 10          |
  | 2   | 2015-01-02 | 25          |
  | 3   | 2015-01-03 | 20          |
  | 4   | 2015-01-04 | 30          |

  Output:

  | id  |
  | --- |
  | 2   |
  | 4   |
  ```

## Solution

* sql

  ```sql
  SELECT weather.id AS 'Id' FROM weather
    JOIN weather w ON DATEDIFF(weather.recordDate, w.recordDate) = 1
      AND weather.Temperature > w.Temperature;
  ```
