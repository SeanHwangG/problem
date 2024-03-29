# [LC_remove-boxes](https://leetcode.com/problems/remove-boxes)

* en

  ```en
  Given boxes with different colors represented by different positive numbers
  Repeat until there is no box left
  Each time choose some continuous boxes with same color, remove them and get k x k point, return max possible points
  ```

* tc

  ```tc
  Input: boxes = [1,3,2,2,2,3,4,3,1]
  Output: 23
  ```

## Solution

* py

  ```py
  def removeBoxes(self, B: List[int]) -> int:
    @lru_cache(None)
    def dp(l, r, k):
      if l > r: return 0
      while l + 1 <= r and B[l] == B[l + 1]:  # Increase both `l` and `k` if they have consecutive colors with `B[l]`
        l += 1
        k += 1
      ans = (k + 1) * (k + 1) + dp(l + 1, r, 0)  # Remove all B which has same with `B[l]`
      for m in range(l + 1, r + 1):  # Try to merge non-contiguous B of same color together
        if B[l] == B[m]:
          ans = max(ans, dp(m, r, k + 1) + dp(l + 1, m - 1, 0))
      return ans

    return dp(0, len(B) - 1, 0)
  ```
