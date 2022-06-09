# [LC_longest-increasing-subsequence](https://leetcode.com/problems/longest-increasing-subsequence)

* en

  ```en
  Given int array nums, return the length of the longest strictly increasing subsequence
  ```

* tc

  ```tc
  Input: nums = [10,9,2,5,3,7,101,18]
  Output: 4
  ```

## Solution

* cpp

  ```cpp
  int lengthOfLIS(vector<int>& nums) {
    vector<int> res; // res[i] keeps track of the smallest tail of subsequences with length i + 1
    for(int i = 0; i < nums.size(); i++) {
      auto it = lower_bound(res.begin(), res.end(), nums[i]);
      if (it == res.end()) res.push_back(nums[i]);
      else *it = nums[i];
    }
    return res.size();
  }
  ```

* py

  ```py
  def lengthOfLIS(self, nums):
    dp = [10 ** 10] * (len(nums) + 1)
    for elem in nums:
      dp[bisect_left(dp, elem)] = elem
    return dp.index(10 ** 10)
  ```
