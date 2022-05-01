# [HR_awk-1](https://www.hackerrank.com/challenges/awk-1)

For each student, if one or more of the three scores is missing
Display Not all scores are available for [Identifier]

```txt
Input:
A 25 27 50
B 35 75
C 75 78
D 99 88 76

Output:
Not all scores are available for B
Not all scores are available for C
```

## Solution

* sh

  ```sh
  awk '{if (NF < 4){print "Not all scores are available for "$1}}'
  ```
