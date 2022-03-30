# [LC_maximum-xor-for-each-query](https://leetcode.com/problems/maximum-xor-for-each-query)

Given a sorted array of n non-negative integers and an integer maximumBit, perform following query n times:
Find non-negative int k < 2 maximumBit ST nums[0]^...^nums[nums.length-1] ^ k is maximized
  k is answer to the ith query
Remove last element from current array nums, Return answer, where answer[i] is answer to ith query

```txt
Input: nums = [0,1,1,3], maximumBit = 2
Output: [0,3,2,3]  # [0 ^ 1 ^ 1 ^ 3, 3 ^ 0 ^ 1 ^ 1, 2 ^ 0 ^ 1, 3 ^ 0]
```

## Solution

```cpp
vector<int> getMaximumXor(vector<int>& n, int maximumBit) {
  vector<int> res(n.size());
  int val = (1 << maximumBit) - 1;
  for (int i = 0; i < n.size(); ++i)
    res[n.size() - i - 1] = val ^= n[i];
  return res;
}
```
