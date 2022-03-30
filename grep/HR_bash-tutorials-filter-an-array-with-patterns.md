# [HR_bash-tutorials-filter-an-array-with-patterns](https://www.hackerrank.com/challenges/bash-tutorials-filter-an-array-with-patterns)

Given list of countries, each on new line, filter out names containing 'a' or 'A'

```txt
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

```sh
grep -vi 'a' || printf "\n"
```
