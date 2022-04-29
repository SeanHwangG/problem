# [LC_restore-the-array](https://leetcode.com/problems/restore-the-array)

Program was supposed to print an array of integers
Array is printed as string of digits s and all integers in array were in the range [1, k] without leading zero
Given string s and integer k, return $ possible arrays that can be printed as s using the mentioned program
Since answer may be very large, return it modulo 109 + 7.

```txt
Input: s = "1000", k = 10000
Output: 1

Input: s = "1000", k = 10
Output: 0

Input: s = "1317", k = 2000
Output: 8
```

## Solution

```py
def numberOfArrays(self, s: str, k: int) -> int:
  N, s = len(s), [*map(int, s)] + [math.inf]
  dp = [0] * N + [1]
  for i in range(N - 1, -1, -1):
    num, j = s[i], i + 1
    while 1 <= num <= k and j < N + 1:
      dp[i] = (dp[i] + dp[j]) % 1000000007
      num = 10 * num + s[j]
      j += 1
  return dp[0]
```
