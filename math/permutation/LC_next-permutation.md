# [LC_next-permutation](https://leetcode.com/problems/next-permutation)

```en
Print next permutation
```

```txt
Input: nums = [1,2,3]
Output: [1,3,2]
```

## Solution

* cpp

  ```cpp
  void nextPermutation(vector<int>& nums) {
    next_permutation(begin(nums), end(nums));
  }
  ```

* py

  ```py
  def nextPermutation(self, nums):
    i = j = len(nums)-1   # 1: find sorted until
    while i > 0 and nums[i-1] >= nums[i]:
      i -= 1
    if i == 0:
      nums.reverse()
      return
    k = i - 1  # find the last "ascending" position
    while nums[j] <= nums[k]:
      j -= 1
    nums[k], nums[j] = nums[j], nums[k]
    l, r = k+1, len(nums)-1  # reverse the second part
    while l < r:
      nums[l], nums[r] = nums[r], nums[l]
      l +=1 ; r -= 1
  ```
