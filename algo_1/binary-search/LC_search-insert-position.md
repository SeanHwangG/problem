# [LC_search-insert-position](https://leetcode.com/problems/search-insert-position)

* en

  ```en
  Search for insertion point
  ```

* tc

  ```tc
  Input: nums = [1,3,5,6], target = 7
  Output: 4
  ```

## Solution

* py

  ```py
  def searchInsert(self, nums, target):
    return bisect.bisect_left(nums, target)
  ```
