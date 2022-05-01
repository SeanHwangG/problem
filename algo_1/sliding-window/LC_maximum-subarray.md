# [LC_maximum-subarray](https://leetcode.com/problems/maximum-subarray)

Given an integer array nums, find the contiguous subarray which has the largest sum and return its sum

```txt
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
```

## Solution

* java
  * Run; O(N)

  ```java
  public static int maxSubArray(int[] A) {
    int maxSoFar = A[0], maxEndingHere = A[0];
    for (int i = 1; i < A.length; ++i){
      maxEndingHere = Math.max(maxEndingHere + A[i], A[i]);
      maxSoFar = Math.max(maxSoFar, maxEndingHere);
    }
    return maxSoFar;
  }
  ```

* py

  ```py
  def maxSubArray(self, nums: List[int]) -> int:
    for i in range(1, len(nums)):
      if nums[i - 1] > 0:
        nums[i] += nums[i - 1]
      return max(nums)
  ```
