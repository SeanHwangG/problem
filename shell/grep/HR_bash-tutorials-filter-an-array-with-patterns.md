# [HR_bash-tutorials-filter-an-array-with-patterns](https://www.hackerrank.com/challenges/bash-tutorials-filter-an-array-with-patterns)

* en

  ```en
  Given list of countries, each on new line, filter out names containing 'a' or 'A'
  ```

* tc

  ```tc
  Input:
  Namibia
  Nauru
  Nepal
  Netherlands
  NewZealand
  Nicaragua
  Niger
  Nigeria
  NorthKorea
  Norway

  Output: Niger
  ```

## Solution

* sh

  ```sh
  grep -vi 'a' || printf "\n"
  ```
