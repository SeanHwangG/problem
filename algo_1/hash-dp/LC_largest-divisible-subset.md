# [LC_largest-divisible-subset](https://leetcode.com/problems/largest-divisible-subset)

* en

  ```en
  Find largest divisible subset s.t. every pair (answer[i], answer[j]) in this subset satisfies
  answer[i] % answer[j] == 0, or answer[j] % answer[i] == 0
  ```

* tc

  ```tc
  Input: nums = [1,2,3]
  Output: [1,2]
  ```

## Solution

* py

  ```py
  def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    S = {-1: set()}
    for x in sorted(nums):
      S[x] = max((S[d] for d in S if x % d == 0), key = len) | {x}
    return list(max(S.values(), key=len))
  ```
