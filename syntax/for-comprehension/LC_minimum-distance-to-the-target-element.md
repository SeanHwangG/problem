# [LC_minimum-distance-to-the-target-element](https://leetcode.com/problems/minimum-distance-to-the-target-element)

Given an int array and two integers target and start
Find an index i such that nums[i] == target and abs(i - start) is minimized
Return abs(i - start)

```txt
Input: nums = [1,2,3,4,5], target = 5, start = 3
Output: 1
```

## Solution

* Time; O(n)
* Space; O(1)

* py

  ```py
  def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
    return min(abs(start - i) for i, n in enumerate(nums) if n == target)
  ```
