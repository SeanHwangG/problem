# [LC_check-if-number-is-a-sum-of-powers-of-three](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three)

Given an integer n, check if it is possible to represent n as the sum of distinct powers of three

```txt
Input:
9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1

Output:
10
12
11
```

## Solution

```py
def checkPowersOfThree(self, n: int) -> bool:
  while n > 1:
    n, r = divmod(n, 3)
    if r == 2: return False
  return True
```
