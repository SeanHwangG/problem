# [LC_subarray-sum-equals-k](https://leetcode.com/problems/subarray-sum-equals-k)

Given array of int nums and int k, return total # continuous subarrays whose sum equals to k

```txt
Input: nums = [1,1,1], k = 2
Output: 2
```

## Solution

```py
def subarraySum(self, nums: List[int], k: int) -> int:
  count, cur, res = {0: 1}, 0, 0
  for v in nums:
    cur += v
    res += count.get(cur - k, 0)
    count[cur] = count.get(cur, 0) + 1
  return res
```
