# [LC_minimum-number-of-increments-on-subarrays-to-form-a-target-array](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array)

Given array of positive integers target and an array initial of same size with all zeros
Return minimum # operations to form target array from initial if you are allowed to do the following operation:
Choose any subarray from initial and increment each value by one

```txt
Input: target = [1,2,3,2,1]
Output: 3  # [0,0,0,0,0] -> [1,1,1,1,1] -> [1,2,2,2,1] -> [1,2,3,2,1]

Input: target = [3,1,1,2]
Output: 4  # [0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2]
```

## Solution

* py

  ```py
  def minNumberOperations(self, A: List[int]) -> int:
    return sum(max(b - a, 0) for b, a in zip(A, [0] + A))
  ```
