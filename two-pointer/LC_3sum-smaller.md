# [LC_3sum-smaller](https://leetcode.com/problems/3sum-smaller)

Given integers and a target
Find number of index triplets i, j, k with 0 <= i < j < k < n st condition nums[i] + nums[j] + nums[k] < target

```txt
Input: nums = [-2,0,1,3], and target = 2
Output: 2
```

## Solution

```py
def threeSumSmaller(self, nums, target):
  count = 0
  nums.sort()
  for i in range(len(nums)):
    j, k = i + 1, len(nums)-1
    while j < k:
      s = nums[i] + nums[j] + nums[k]
      if s < target:
        count += k-j # if (i,j,k) works, then (i,j,k), (i,j,k-1) ... (i, j, j + 1)
        j += 1
      else:
        k -= 1
  return count
```
