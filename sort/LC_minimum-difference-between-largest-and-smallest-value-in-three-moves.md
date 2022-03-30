# [LC_minimum-difference-between-largest-and-smallest-value-in-three-moves](https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves)

Given array nums, you can choose 1 element and change it by any value in one move
Return min difference between largest and smallest value of nums after perfoming at most 3 moves

```txt
Input: nums = [5,3,2,4]
Output: 0

Input: nums = [1,5,0,10,14]
Output: 1

Input: nums = [6,6,0,1,1,4,6]
Output: 2
```

## Solution

```py
def minDifference(self, A):
  A.sort()
  return min(b - a for a, b in zip(A[:4], A[-4:]))
```
