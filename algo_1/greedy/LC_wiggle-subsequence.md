# [LC_wiggle-subsequence](https://leetcode.com/problems/wiggle-subsequence)

* en

  ```en
  Wiggle sequence is sequence where differences between successive numbers strictly alternate between positive and negative
  The first difference may be either positive or negative. One element is trivially a wiggle sequence
  Find length of longest wiggle sequence
  ```

* tc

  ```tc
  Input: nums = [1,7,4,9,2,5]
  Output: 6
  ```

## Solution

* py

  ```py
  def wiggleMaxLength(self, nums: List[int]) -> int:
    len_dec, len_inc = 1, 1
    for i in range(1, len(nums)):
      len_dec = len_inc + 1 if nums[i] < nums[i-1] else len_dec
      len_inc = len_dec + 1 if nums[i] > nums[i-1] else len_inc
    return max(len_inc, len_dec)
  ```
