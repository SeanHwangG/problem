# [LC_range-sum-query-immutable](https://leetcode.com/problems/range-sum-query-immutable)

* en

  ```en
  Implement the NumArray class:
  NumArray(int[] nums) Initializes the object with the integer array nums.
  int sumRange(int left, int right) Returns sum of elements of nums between indices left and right inclusive
    (ex: nums[left] + nums[left + 1] + ... + nums[right]).
  ```

* tc

  ```tc
  Input:
  ["NumArray", "sumRange", "sumRange", "sumRange"]
  [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

  Output: [null, 1, -1, -3]
  ```

## Solution

* py

  ```py
  class NumArray:
    def __init__(self, nums: List[int]):
      summ = 0
      self.prefix = [summ := summ + num for num in nums]

    def sumRange(self, i: int, j: int) -> int:
      return self.prefix[j] - (self.prefix[i - 1] if i > 0 else 0)
  ```
