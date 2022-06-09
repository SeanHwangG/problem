# [LC_split-array-with-equal-sum](https://leetcode.com/problems/split-array-with-equal-sum)

* en

  ```en
  Given an integer array nums of length n, return if there is a triplet (i, j, k) which satisfies the following conditions:
  0 < i, i + 1 < j, j + 1 < k < n - 1
  Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) is equal.
  Subarray (l, r) represents a slice of original array starting from element indexed l to element indexed r
  ```

* tc

  ```tc
  Input: nums = [1,2,1,2,1,2,1]
  Output: true  # i = 1, j = 3, k = 5

  Input: nums = [1,2,1,2,1,2,1,2]
  Output: false
  ```

## Solution

* py

  ```py
  def splitArray(self, nums: list):
    def split(A):
      total = sum(A)
      for i in range(1, len(A)): A[i] += A[i - 1]
      return {A[i - 1] for i in range(1, len(A) - 1) if A[i - 1] == total - A[i]}
    return any(split(nums[:j]) & split(nums[j+1:]) for j in range(3, len(nums)-3))
  ```
