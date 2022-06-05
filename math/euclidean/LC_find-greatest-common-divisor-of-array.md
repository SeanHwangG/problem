# [LC_find-greatest-common-divisor-of-array](https://leetcode.com/problems/find-greatest-common-divisor-of-array)

```en
Given an integer array nums, return greatest common divisor of smallest number and largest number in nums
greatest common divisor of two numbers is largest positive integer that evenly divides both numbers
```

```txt
Input: nums = [2,5,6,9,10]
Output: 2

Input: nums = [7,5,6,8,3]
Output: 1
```

## Solution

* py

  ```py
  def findGCD(self, nums: List[int]) -> int:
    return gcd(min(nums), max(nums))
  ```
