# [LC_reverse-pairs](https://leetcode.com/problems/reverse-pairs)

* en

  ```en
  Given an integer array nums, return the number of reverse pairs in the array
  Reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 x nums[j]
  ```

* tc

  ```tc
  Input: nums = [2,4,3,5,1]
  Output: 3
  ```

## Solution

* py

  ```py
  class BIT:
    def __init__(self, n):
      self.n = n + 1
      self.sums = [0] * self.n

    def update(self, i, delta):
      while i < self.n:
        self.sums[i] += delta
        i += i & (-i)

    def query(self, i):
      res = 0
      while i > 0:
        res += self.sums[i]
        i -= i & (-i)
      return res

  def reversePairs(self, nums):
    # BIT O(nlogn)
    new_nums = nums + [x * 2 for x in nums]
    sorted_set = sorted(list(set(new_nums)))
    tree = self.BIT(len(sorted_set))
    res = 0
    ranks = {}
    for i, n in enumerate(sorted_set):
      ranks[n] = i + 1

    for n in nums[::-1]:
      res += tree.query(ranks[n] - 1)
      tree.update(ranks[n * 2], 1)

    return res
  ```
