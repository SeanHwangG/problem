# [LC_jump-game](https://leetcode.com/problems/jump-game)

Given an array of non-negative integers nums, you are initially positioned at the first index of the array
Each element in the array represents your maximum jump length at that position

```txt
Input: nums = [2,3,1,1,4]
Output: true
```

## Solution

```py
def canJump(self, nums: List[int]) -> bool:
  pos = 0
  for i, n in enumerate(nums):
    if i <= pos:
      pos = max(pos, i + n)
  return len(nums) - 1 <= pos
```
