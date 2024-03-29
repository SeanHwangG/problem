# [LC_range-sum-query-mutable](https://leetcode.com/problems/range-sum-query-mutable)

* en

  ```en
  Design class with following methods
    NumArray(int[] nums) initializes the object with the integer array nums
    void update(int index, int val) updates the value of nums[index] to be val
    int sumRange(int left, int right) returns the sum of the subarray nums[left, right]
      (i.e., nums[left] + nums[left + 1], ..., nums[right])
  At most 3 * 10^4 calls will be made to update and sumRange
  ```

* tc

  ```tc
  Input:
  ["NumArray", "sumRange", "update", "sumRange"]
  [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]

  Output: [null, 9, null, 8]
  ```

## Solution

* py

  ```py
  class NumArray(object):
    def __init__(self, nums):
      self.n = len(nums)
      self.a, self.c = nums, [0] * (self.n + 1)
      for i in range(self.n):
        k = i + 1
        while k <= self.n:
          self.c[k] += nums[i]
          k += (k & -k)

    def update(self, i, val):
      diff, self.a[i] = val - self.a[i], val
      i += 1
      while i <= self.n:
        self.c[i] += diff
        i += (i & -i)

    def sumRange(self, i, j):
      res, j = 0, j + 1
      while j:
        res += self.c[j]
        j -= (j & -j)
      while i:
        res -= self.c[i]
        i -= (i & -i)
      return res
  ```
