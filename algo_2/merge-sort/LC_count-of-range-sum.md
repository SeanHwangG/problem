# [LC_count-of-range-sum](https://leetcode.com/problems/count-of-range-sum)

* en

  ```en
  Given int array nums and two integers lower and upper, return # range sums that lie in [lower, upper] inclusive
  Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j
  ```

* tc

  ```tc
  Input: nums = [-2,5,-1], lower = -2, upper = 2
  Output: 3  # [0,0], [2,2], and [0,2]
  ```

## Solution

* py

  ```py
  def countRangeSum(self, nums, lower, upper):
    first = [0]
    for num in nums:
      first.append(first[-1] + num)
    def sort(lo, hi):
      mid = (lo + hi) / 2
      if mid == lo:
        return 0
      count = sort(lo, mid) + sort(mid, hi)
      i = j = mid
      for left in first[lo:mid]:
        while i < hi and first[i] - left < lower: i += 1
        while j < hi and first[j] - left <= upper: j += 1
        count += j - i
      first[lo:hi] = sorted(first[lo:hi])
      return count
    return sort(0, len(first))
  ```
