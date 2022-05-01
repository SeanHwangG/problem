# [LC_single-number-iii](https://leetcode.com/problems/single-number-iii)

Given int array nums, in which exactly 2 elements appear only once and all the other elements appear exactly twice
Find the two elements that appear only once. You can return the answer in any order

```txt
Input: nums = [1,2,1,3,2,5]
Output: [3,5]  # [5, 3] is also a valid answer.
```

## Solution

* cpp

  ```cpp
  class Solution {
  public:
    vector<int> singleNumber(vector<int>& nums) {
      int xored = accumulate(nums.begin(), nums.end(), 0, bit_xor<int>());
      xored &= -xored;
      vector<int> ret = {0, 0};
      for (int num : nums){
        if (xored & num) ret[0] ^= num;
        else             ret[1] ^= num;
      }
      return ret;
    }
  };
  ```
