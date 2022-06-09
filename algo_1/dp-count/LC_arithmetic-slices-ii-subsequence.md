# [LC_arithmetic-slices-ii-subsequence](https://leetcode.com/problems/arithmetic-slices-ii-subsequence)

* en

  ```en
  Given an integer array nums, return the number of all the arithmetic subsequences of length greater than 2
  ```

* tc

  ```tc
  Input: nums = [2,4,6,8,10]
  Output: 7
  ```

## Solution

* py

  ```py
  def numberOfArithmeticSlices(self, li: List[int]) -> int:
    ans = 0
    dp = defaultdict(int)
    for i in range(1, len(li)):
      for j in range(i):
        delta = li[i] - li[j]
        ans += dp[(j, delta)]
        dp[(i, delta)] += dp[(j, delta)] + 1

    return ans
  ```
