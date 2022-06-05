# [LC_house-robber](https://leetcode.com/problems/house-robber)

```en
Each house has a certain amount of money stashed
Adjacent houses have security systems connected
Automatically contact the police if two adjacent houses were broken into on the same night
```

```txt
Input: nums = [1,2,3,1]
Output: 4
```

## Solution

* java

  ```java
  public int rob(int[] nums) {
    if (nums.length == 0)   return 0;

    int N_best = 0, Y_best = nums[0];

    for (int i = 1; i < nums.length; i++){
      int temp = N_best;
      N_best = Math.max(N_best, Y_best);
      Y_best = temp + nums[i];
    }
    return Math.max(N_best, Y_best);
  }
  ```
