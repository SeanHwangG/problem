# [HR_japanese-cities-name](https://www.hackerrank.com/challenges/japanese-cities-name)

* en

  ```en
  Names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN
  ```

* tc

  ```tc
  Input:
  | Id   | City       | Country | State        | Zip    |
  | ---- | ---------- | ------- | ------------ | ------ |
  | 6    | Rotterdam  | JPN     | Zuid-Holland | 593321 |
  | 1661 | Ecottsdale | USA     | Arizona      | 202705 |
  | 3965 | Corona     | USA     | California   | 124966 |

  Output:
  | Id   | City       | Country | State        | Zip    |
  | ---- | ---------- | ------- | ------------ | ------ |
  | 6    | Rotterdam  | JPN     | Zuid-Holland | 593321 |
  | 1661 | Ecottsdale | USA     | Arizona      | 202705 |
  | 3965 | Corona     | USA     | California   | 124966 |
  ```

## Solution

* sql

  ```sql
  SELECT Name FROM City WHERE CountryCode = 'JPN';
  ```
