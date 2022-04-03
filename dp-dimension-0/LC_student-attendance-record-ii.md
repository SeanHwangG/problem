# [LC_student-attendance-record-ii](https://leetcode.com/problems/student-attendance-record-ii)

An attendance record for a student can be represented as string: 'A': Absent / 'L': Late / 'P': Present
Any student is eligible for an attendance award if they meet both of the following criteria:
  Student was absent ('A') for strictly fewer than 2 days total.
  Student was never late ('L') for 3 or more consecutive days.
Given n, return # possible attendance records MOD 1e9 + 7 of length n that make student eligible for attendance award

```txt
Input: n = 2
Output: 8  # "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
```

## Solution

```py
class Solution(object):
  def checkRecord(self, N):
    MOD = 10 ** 9 + 7
    a = b = d = 1  # without an 'A' ending in N, NL, LL
    c = e = f = 0  # with an 'A' ending in N, NL, LL
    for _ in range(N-1):
      a, b, c, d, e, f = (a + b + c) % MOD, a, b, (a + b + c + d + e + f) % MOD, d, e
    return (a + b + c + d + + e + f) % MOD
```
