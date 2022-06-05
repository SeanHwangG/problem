# [LC_big-countries](https://leetcode.com/problems/big-countries)

```en
Country is big if it has area of bigger than 3 million square km or a population of more than 25 million
Output big countries' name, population and area
```

```txt
Input:
| name        | continent | area    | population | gdp       |
| ----------- | --------- | ------- | ---------- | --------- |
| Afghanistan | Asia      | 652230  | 25500100   | 20343000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000 |
| Andorra     | Europe    | 468     | 78115      | 3712000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000 |

Output:
| name        | population | area    |
| ----------- | ---------- | ------- |
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
```

## Solution

* sql

  ```sql
  SELECT name, population, area FROM World
    WHERE 3000000 < area OR 25000000 < population;
  ```
