# [LC_third-maximum-number](https://leetcode.com/problems/third-maximum-number)

Given integer array nums, return third maximum number in this array
If third maximum does not exist, return maximum number

```txt
Input: nums = [2,2,3,1]
Output: 1
```

## Solution

```py
def thirdMax(self, nums):
  a = b = c = -float("inf")
  for n in nums:
    if n in (a, b, c): continue
    if n > a:
      n, a = a, n
    if n > b
     n, b = b, n
    if n > c:
      n, c = c, n
  return a if c == -float("inf") else c
```
