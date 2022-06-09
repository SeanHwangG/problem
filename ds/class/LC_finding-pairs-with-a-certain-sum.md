# [LC_finding-pairs-with-a-certain-sum](https://leetcode.com/problems/finding-pairs-with-a-certain-sum)

* en

  ```en
  Given two integer arrays nums1 and nums2, implement a data structure that supports queries of two types:
    Add a positive integer to an element of a given index in the array nums2
    Count the number of pairs (i, j) s.t. nums1[i] + nums2[j] equals a given value
  ```

* tc

  ```tc
  Input:
  ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
  [[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]

  Output:
  [null, 8, null, 2, 1, null, null, 11]
  ```

## Solution

* py

  ```py
  class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
      self.c1, c2 = Counter(nums1), Counter(nums2)
      self.l2 = nums2

    def add(self, idx: int, val: int) -> None:
      self.c2[self.l2[idx]] -= 1
      self.l2[idx] += val
      self.c2[self.l2[idx]] += 1

    def count(self, tot: int) -> int:
      return sum(v * self.c2[tot - k] for k, v in self.c1.items())
  ```
