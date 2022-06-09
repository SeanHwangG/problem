# [LC_4sum](https://leetcode.com/problems/4sum)

* en

  ```en
  Given array nums of n int and target, find unique set of a, b, c, and d that sums up to target
  ```

* tc

  ```tc
  Input: nums = [1,0,-1,0,-2,2], target = 0
  Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
  ```

## Solution

* py

  ```py
  def fourSum(self, nums, target):
    def findNsum(nums, target, N, cur, results):
      if len(nums) == 0 or not (nums[0] * N <= target <= nums[-1] * N):
        return
      if N == 2:
        l, r = 0, len(nums) - 1
        while l < r:
          s = nums[l] + nums[r]
          if s == target:
            results.append(cur + [nums[l], nums[r]])
            l += 1
            while l < r and nums[l] == nums[l-1]:
              l += 1
          elif s < target:    l += 1
          else:               r -= 1
      else:
        for i in range(len(nums) - N + 1):
          if i == 0 or nums[i - 1] != nums[i]:
            findNsum(nums[i + 1:], target - nums[i], N - 1, cur + [nums[i]], results)

    results = []
    findNsum(sorted(nums), target, 4, [], results)
    return results
  ```
