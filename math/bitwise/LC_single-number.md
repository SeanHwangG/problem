# [LC_single-number](https://leetcode.com/problems/single-number)

```en
Find only number where all other numbers appear twice
```

```txt
Input: nums = [0,1,0,1,99]
Output: 99
```

## Solution

* cpp

  ```cpp
  int singleNumber(vector<int>& nums) {
    return accumulate(begin(nums), end(nums), 0, bit_xor<int>());
  };
  ```

* py

  ```py
  def singleNumber(self, nums: List[int]) -> int:
    return reduce(lambda x, y: x ^ y, nums)
  ```
