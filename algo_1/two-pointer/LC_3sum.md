# [LC_3sum](https://leetcode.com/problems/3sum)

* en

  ```en
  Find list of three indices that sums up to zero
  ```

* tc

  ```tc
  Input: nums = [-1,2,1,-4], target = 1
  Output: 2
  ```

## Solution

* py

  ```py
  def threeSum(self, nums):
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
      if i > 0 and nums[i] == nums[i-1]: continue
      l, r = i + 1, len(nums) - 1
      while l < r:
        s = nums[i] + nums[l] + nums[r]
        if s == 0:
          res.append([nums[i] ,nums[l] ,nums[r]])
          l += 1; r -= 1
          while l < r and nums[l] == nums[l - 1]: l += 1
          while l < r and nums[r] == nums[r + 1]: r -= 1
        elif s < 0:
          l += 1
        else:
          r -= 1
    return res
  ```
