# [LC_split-array-largest-sum](https://leetcode.com/problems/split-array-largest-sum)

* en

  ```en
  Given array nums which consists of non-negative integers and integer m, split array into m non-empty continuous subarrays
  Minimize the largest sum among these m subarrays
  ```

* tc

  ```tc
  Input: nums = [7,2,5,10,8], m = 2
  Output: 18
  ```

## Solution

* py

  ```py
  def is_valid(self, nums, m, mi):
    cuts, curr_sum = 0, 0
    for x in nums:
      curr_sum += x
      if curr_sum > mi:
        cuts, curr_sum = cuts + 1, x
    subs = cuts + 1
    return subs <= m

  def splitArray(self, nums, m):
    lo, hi, ans = max(nums), sum(nums), -1
    while lo <= hi:
      mi = (lo + hi) // 2
      if self.is_valid(nums, m, mi):
        ans, hi = mi, mi - 1
      else:
        lo = mi + 1
    return ans
  ```
