# [HR_awk-2](https://www.hackerrank.com/challenges/awk-2)

Student is considered to have passed if (s)he has a score 50 or more in each of the three subjects
display the following for each student: `[Identifier]: [Pass/Fail]`

```txt
Input:
A 25 27 50
B 35 37 75
C 75 78 80
D 99 88 76

Output:
A : Fail
B : Fail
C : Pass
D : Pass
```

## Solution

```sh
awk '{print $1,":", ($2<50||$3<50||$4<50) ? "Fail" : "Pass"}'
```
