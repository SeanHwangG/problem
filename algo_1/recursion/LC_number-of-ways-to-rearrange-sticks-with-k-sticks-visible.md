# [LC_number-of-ways-to-rearrange-sticks-with-k-sticks-visible](https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible)

* en

  ```en
  There are n uniquely-sized sticks whose lengths are integers from 1 to n
  arrange the sticks such that exactly k sticks are visible from the left
  Given n and k, return the number of such arrangements modulo 10e9 + 7
  ```

* tc

  ```tc
  Input: n = 3, k = 2
  Output: 3  # [1,3,2], [2,3,1], and [2,1,3] exactly 2 sticks are visible
  ```

## Solution

* py

  ```py
  @lru_cache(None)
  def rearrangeSticks(self, n: int, k: int) -> int:
    if k < 0 or n == 0: return k == 0
    return (self.rearrangeSticks(n - 1, k) * (n - 1) + self.rearrangeSticks(n - 1, k - 1)) % int(1e9 + 7)
  ```
