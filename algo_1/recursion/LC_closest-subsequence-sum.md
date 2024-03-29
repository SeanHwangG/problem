# [LC_closest-subsequence-sum](https://leetcode.com/problems/closest-subsequence-sum)

* en

  ```en
  Given int array nums and an integer goal
  Choose subsequence of nums such that the sum of its elements is the closest possible to goal
  That is, if sum of subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal)
  Return min possible value of abs(sum - goal)
  ```

* tc

  ```tc
  Input: nums = [5,-7,3,5], goal = 6
  Output: 0
  ```

## Solution

* py

  ```py
  def minAbsDifference(self, nums: List[int], goal: int) -> int:
    def generate_sum(nums):
      ans = {0}
      for x in nums:
        ans |= {x + y for y in ans}
      return ans

    evens = [-inf, *sorted(generate_sum(nums[::2])), inf]

    return min(abs(y + x - goal)
                for x in generate_sum(nums[1::2])
                for k in [bisect_left(evens, goal - x)]
                for y in evens[k - 1 : k + 1])
  ```
