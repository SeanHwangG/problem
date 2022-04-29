# [LC_constrained-subsequence-sum](https://leetcode.com/problems/constrained-subsequence-sum)

Given int array nums and int k, return the maximum sum of a non-empty subsequence
ST for every two consecutive int in subsequence, nums[i] and nums[j], where i < j, condition j - i <= k is satisfied

```txt
Input: nums = [10,2,-10,5,20], k = 2
Output: 37  # The subsequence is [10, 2, 5, 20].

Input: nums = [-1,-2,-3], k = 1
Output: -1

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23  # The subsequence is [10, -2, -5, 20].
```

## Solution

* Time; O(N)

* py

```py
def constrainedSubsetSum(self, dp: List[int], k: int) -> int:
  dq = deque()  # stores dp[i - k], dp[i - k + 1], .., dp[i - 1] whose values are larger than 0 in decreasing order
  for i in range(len(dp)):
    dp[i] += dq[0] if dq else 0  # maximum result if last element is dp[i]
    while len(dq) and dp[i] > dq[-1]:
      dq.pop()
    if dp[i] > 0:
      dq.append(dp[i])
    if i >= k and dq and dq[0] == dp[i - k]:  # Don't need dp[i - k] when computing dp[i + 1], to satisfy j - i <= k
      dq.popleft()
  return max(dp)
```
