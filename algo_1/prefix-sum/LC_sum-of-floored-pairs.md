# [LC_sum-of-floored-pairs](https://leetcode.com/problems/sum-of-floored-pairs)

Given int array, return sum of floor(nums[i] / nums[j]) for all pairs 0 <= i, j < nums.length MOD 10^9+7
The floor() function returns the integer part of the division.

```txt
Input: nums = [2,5,9]
Output: 10

Input: nums = [7,7,7,7,7,7,7]
Output: 49
```

## Solution

* py

  ```py
  def sumOfFlooredPairs(self, nums: List[int]) -> int:
    incs, co = [0] * (max(nums) + 1), Counter(nums)  # To store all the quotients increases
    for num in co:
      for j in range(num, len(incs), num):  # Loop over all the possible dividends where the quotient increases
        incs[j] += co[num]  # Increment the increases in quotients
    quots = list(accumulate(incs))  # Accumulate the increases to get the sum of quotients
    return sum([quots[num] for num in nums]) % 1_000_000_007  # Sum up all the quotients for all the numbers in the list
  ```
