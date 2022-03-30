# [LC_minimum-operations-to-make-the-array-increasing](https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing)

Given integer array nums (0-indexed). In 1 operation, choose an element of array and increment it by 1
Return minimum number of operations needed to make nums strictly increasing

```txt
Input: nums = [1,1,1]
Output: 3
```

## Solution

```cpp
int minOperations(vector<int>& nums) {
  int res = 0, last = 0;
  for (auto n : nums) {
    res += max(0, last - n + 1);
    last = max(n, last + 1);
  }
  return res;
}
```
