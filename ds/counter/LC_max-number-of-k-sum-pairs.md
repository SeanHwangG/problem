# [LC_max-number-of-k-sum-pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs)

* en

  ```en
  Given an integer array nums and an integer k
  In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array
  Return the maximum number of operations you can perform on the array

  ```

* tc

  ```tc
  Input: nums = [1,2,3,4], k = 5
  Output: 2
  ```

## Solution

* cpp

  ```cpp
  int maxOperations(vector<int>& nums, int k) {
    unordered_map<int, int> num2count;
    for (auto &num: nums) num2count[num]++;  // count freq of nums
    int ans = 0;

    for(auto it = num2count.begin(); it != num2count.end(); ++it){
      int num = it->first, count = it->second;
      if (k - num == num) ans += count/2;   // if num is half of k add half of it's count in ans
      else if (num2count.count(k - num)){   // find k-num in nums and add min freq of num or k-num to ans
        int mn = min(count, num2count[k-num]);
        ans += mn;
        num2count[num] -= mn;
        num2count[k-num] -= mn;
      }
    }

    return ans;
  }
  ```

* py

  ```py
  from collections import Counter
  class Solution:
    def maxOperations(self, nums: List[int], target: int) -> int:
      co, ret = Counter(nums), 0
      for n in co:
        if n <= target // 2:
          ret += co[target - n] // 2 if n * 2 == target else min(co[n], co[target - n])
      return ret
  ```
