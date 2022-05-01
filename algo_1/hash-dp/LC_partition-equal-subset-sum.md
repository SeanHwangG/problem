# [LC_partition-equal-subset-sum](https://leetcode.com/problems/partition-equal-subset-sum)

Check whether it can be splitted into two equal sum array

```txt
Input: nums = [1,5,11,5]
Output: true
```

## Solution

* py

  ```py
  def canPartition(nums):
    if sum(nums) & 1 == 0:
      target = sum(nums) >> 1
      dp = {0}
      for i in nums:
        dp |= {i + x for x in dp}
        if target in dp:
          return True
    return False
  ```
