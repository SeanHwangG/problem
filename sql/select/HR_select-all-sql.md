# [HR_select-all-sql](https://www.hackerrank.com/challenges/select-all-sql)

Select all city information

```txt
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

```sql
SELECT * FROM City;
```
