# [LC_jump-game-ii](https://leetcode.com/problems/jump-game-ii)

* en

  ```en
  Given non-negative integers nums, each num represents your maximum jump length at that idx
  From the first idx, find the the minimum number of jumps to reach the last index
  ```

* tc

  ```tc
  Input: nums = [2,3,1,1,4]
  Output: 2
  ```

## Solution

* Time, Space; O(N), O(1)

* py

  ```py
  def jump(self, nums):
    l, r = 0, nums[0]
    time = 1
    while r < len(nums) - 1:
      time += 1
      nxt = max(i + nums[i] for i in range(l, r + 1))
      l, r = r, nxt # nxt : farthest point that all points in [l, r] can reach
    return time
  ```
