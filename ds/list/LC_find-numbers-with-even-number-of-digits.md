# [LC_find-numbers-with-even-number-of-digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits)

```en
Given an array nums of integers, return how many of them contain an even number of digits

```

```txt
Input: nums = [12,345,2,6,7896]
Output: 2  # 12, 7896

Input: nums = [555,901,482,1771]
Output: 1  # 1771 contains even number of digit

```

## Solution

* cpp

  ```cpp
  int findNumbers(vector<int>& nums) {
    return accumulate(nums.cbegin(), nums.cend(), 0,
      [](auto a, auto b) {
        return a + (to_string(b).size() % 2 == 0);
      });
  }
  ```

* py

  ```py
  def findNumbers(self, nums: List[int]) -> int:
    return len([i for i in nums if len(str(i)) % 2 == 0])
  ```
