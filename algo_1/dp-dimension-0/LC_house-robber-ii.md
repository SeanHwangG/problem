# [LC_house-robber-ii](https://leetcode.com/problems/house-robber-ii)

* en

  ```en
  Each house, in circle, has a certain amount of money stashed
  Adjacent houses have security systems connected and it will automatically contact police
    If two adjacent houses were broken into on same night
  Maximize amount of money you can rob
  ```

* tc

  ```tc
  Input: nums = [1,2,3,1]
  Output: 4  # Rob house 1 (money = 1) and then rob house 3 (money = 3).
  ```

## Solution

* cpp

  ```cpp
  int rob(vector<int>& nums) {
    int n = nums.size();
    if (n < 2) return n ? nums[0] : 0;
    return max(robber(nums, 0, n - 2), robber(nums, 1, n - 1));
  }
  int robber(vector<int>& nums, int l, int r) {
    int pre = 0, cur = 0;
    for (int i = l; i <= r; i++) {
      int temp = max(pre + nums[i], cur);
      pre = cur;
      cur = temp;
    }
    return cur;
  }
  ```
