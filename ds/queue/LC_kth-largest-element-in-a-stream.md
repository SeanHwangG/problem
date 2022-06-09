# [LC_kth-largest-element-in-a-stream](https://leetcode.com/problems/kth-largest-element-in-a-stream)

* en

  ```en
  Design a class to find the kth largest element in a stream
  Note that it is the kth largest element in the sorted order, not the kth distinct element
  ```

* tc

  ```tc
  Input:
  ["KthLargest", "add", "add", "add", "add", "add"]
  [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

  Output: [null, 4, 5, 5, 8, 8]
  ```

## Solution

* py

  ```py
  class KthLargest:
    def __init__(self, k: int, nums: List[int]):
      self.pq, self.k = [], k
      for n in nums:
        self.add(n)

    def add(self, val: int) -> int:
      heapq.heappush(self.pq, val)
      if len(self.pq) > self.k:
        heapq.heappop(self.pq)
      return self.pq[0]
  ```
