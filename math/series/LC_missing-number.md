# [LC_missing-number](https://leetcode.com/problems/missing-number)

* en

  ```en
  Given array nums containing n distinct numbers in range [0, n], return only number in range that is missing from array
  ```

* tc

  ```tc
  Input: nums = [3,0,1]
  Output: 2
  ```

## Solution

* py

  ```py
  def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    return n * (n+1) // 2 - sum(nums)
  ```
