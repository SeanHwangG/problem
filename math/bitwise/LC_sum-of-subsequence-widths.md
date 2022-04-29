# [LC_sum-of-subsequence-widths](https://leetcode.com/problems/sum-of-subsequence-widths)

Width of a sequence is the difference between the maximum and minimum elements in the sequence
Given array of integers nums, return sum of widths of all non-empty subsequences of nums modulo 10**9 + 7

```txt
Input: nums = [2,1,3]
Output: 6
```

## Solution

* py

```py
def sumSubseqWidths(self, A: List[int]) -> int:
  A.sort()
  res = 0
  for i in range(len(A)):
    res *= 2
    res += A[~i] - A[i]
    res %= 10 ** 9 + 7
  return res
```
