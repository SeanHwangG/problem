# [LC_3sum-closest](https://leetcode.com/problems/3sum-closest)

* en

  ```en
  Given array S of n int, find three int in S such that the sum is closest to a given number, target
  ```

* tc

  ```tc
  Input: nums = [-1,2,1,-4], target = 1
  Output: 2
  ```

## Solution

* java

  ```java
  public int threeSumClosest(int[] nums, int target) {
    if (nums == null || nums.length < 3) return 0;
    Arrays.sort(nums);
    int sum = 0, closest = nums[0] + nums[1] + nums[2];
    for (int i = 0; i < nums.length - 2; i++) {
      if (i > 1 && nums[i] == nums[i - 1]) continue;
      int lo = i + 1, hi = nums.length - 1;
      while (lo < hi) {
        sum = nums[i] + nums[lo] + nums[hi];
        if (sum == target) return target;
        else if (sum < target) lo++;
        else hi--;
        if (Math.abs(sum - target) < Math.abs(closest - target)) closest = sum;
      }
    }
    return closest;
  }
  ```
