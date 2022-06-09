# [LC_find-k-pairs-with-smallest-sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums)

* en

  ```en
  Given two integer arrays nums1 and nums2 sorted in ascending order and an integer k
  Define a pair (u, v) which consists of one element from first array and one element from second array
  Return k pairs (u1, v1), (u2, v2), ..., (uk, vk) with smallest sums
  ```

* tc

  ```tc
  Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
  Output: [[1,2],[1,4],[1,6]]

  Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
  Output: [[1,1],[1,1]]
  ```

## Solution

* py

  ```py
  def kSmallestPairs(self, nums1, nums2, k):
    streams = map(lambda u: ([u + v, u, v] for v in nums2), nums1)
    stream = heapq.merge(*streams)
    return [suv[1:] for suv in islice(stream, k)]
  ```
