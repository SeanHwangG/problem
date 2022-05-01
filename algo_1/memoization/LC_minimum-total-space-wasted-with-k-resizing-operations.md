# [LC_minimum-total-space-wasted-with-k-resizing-operations](https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations)

Given 0-indexed integer array nums, where nums[i] is the number of elements that will be in the array at time i
In addition, you are given an integer k, the maximum number of times you can resize the array (to any size)
Size of array at time t, sizet, must be at least nums[t] as there needs to be enough space in array to hold all elements
Space wasted at time t is defined as sizet - nums[t], and total space wasted is sum of space wasted time 0<= t< nums.length
Return min total space wasted if you can resize the array at most k times.

```txt
Input: nums = [10,20], k = 0
Output: 10  # size = [20,20].

Input: nums = [10,20,30], k = 1
Output: 10  # size = [20,20,30].

Input: nums = [10,20,15,30,20], k = 2
Output: 15  # size = [10,20,20,30,30].
```

## Solution

* py

  ```py
  def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
    @lru_cache
    def fn(i, k):  # Return min waste from i with k ops
      if len(nums) - i <= k + 1:
        return 0
      if k == 0: return max(nums[i:]) * (len(nums) - i) - sum(nums[i:])
      ans, mx, sm = inf, -inf, 0
      for j in range(i, len(nums)):
        mx = max(mx, nums[j])
        sm += nums[j]
        ans = min(ans, mx * (j - i + 1) - sm + fn(j + 1, k - 1))
      return ans
    return fn(0, k)
  ```
