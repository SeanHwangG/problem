# [LC_maximum-ascending-subarray-sum](https://leetcode.com/problems/maximum-ascending-subarray-sum)

Given an array of positive integers nums, return maximum possible sum of an ascending subarray in nums

```txt
Input: nums = [10,20,30,5,10,50]
Output: 65  # 5 10 50
```

## Solution

```py
def maxAscendingSum(self, nums: List[int]) -> int:
  mx = 0
  for i, x in enumerate(nums):
    if i == 0 or nums[i-1] >= nums[i]: cur = 0
    cur += nums[i]
    mx = max(mx, cur)
  return mx
```
