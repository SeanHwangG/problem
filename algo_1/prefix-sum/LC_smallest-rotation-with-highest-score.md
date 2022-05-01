# [LC_smallest-rotation-with-highest-score](https://leetcode.com/problems/smallest-rotation-with-highest-score)

Score is number of entries that are less than or equal to their index
Return rotation index k that corresponds to the highest score we can achieve if we rotated nums by it
If there are multiple answers, return the smallest such index k.

```txt
Input: nums = [2,3,1,4,0]
Output: 3

Input: nums = [1,3,0,2,4]
Output: 0  # nums will always have 3 points
```

## Solution

* py

  ```py
  def bestRotation(self, A: List[int]) -> int:
    N = len(A)
    change = [1] * N
    for i in range(N):
      change[(i - A[i] + 1) % N] -= 1
    for i in range(1, N):
      change[i] += change[i - 1]
    return change.index(max(change))
  ```
