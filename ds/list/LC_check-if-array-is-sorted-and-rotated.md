# [LC_check-if-array-is-sorted-and-rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated)

* en

  ```en
  Given array nums, return if array was originally sorted in non-decreasing order, then rotated some # positions
  There may be duplicates in the original array
  ```

* tc

  ```tc
  Input: nums = [3,4,5,1,2]
  Output: true
  ```

## Solution

* py

  ```py
  def check(self, nums: List[int]) -> bool:
    return sum(nums[i] < nums[i-1] for i in range(len(nums))) <= 1
  ```
