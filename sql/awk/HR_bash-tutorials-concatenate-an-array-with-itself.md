# [HR_bash-tutorials-concatenate-an-array-with-itself](https://www.hackerrank.com/challenges/bash-tutorials-concatenate-an-array-with-itself)

Concatenate three repetitions of the original array

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

Output:
Namibia Nauru Nepal Netherlands NewZealand Nicaragua Niger Nigeria NorthKorea Norway Namibia Nauru Nepal Netherlands
NewZealand Nicaragua Niger Nigeria NorthKorea Norway Namibia Nauru Nepal Netherlands NewZealand Nicaragua Niger Nigeria
NorthKorea Norway
```

## Solution

```sh
tr `$'\n' ' ' | awk '{print $`0 `$0 $`0}'
```
