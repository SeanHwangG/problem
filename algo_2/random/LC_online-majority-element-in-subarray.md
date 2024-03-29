# [LC_online-majority-element-in-subarray](https://leetcode.com/problems/online-majority-element-in-subarray)

* en

  ```en
  MajorityChecker(int[] arr) constructs an instance of MajorityChecker with the given array arr;
  int query(int left, int right, int threshold) has arguments such that:
  0 <= left <= right < arr.length representing a subarray of arr;
  2 * threshold > right - left + 1, ie. the threshold is always a strict majority of the length of the subarray
  ```

* tc

  ```tc
  MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
  majorityChecker.query(0,5,4); // returns 1
  majorityChecker.query(0,3,3); // returns -1
  majorityChecker.query(2,3,2); // returns 2
  ```

## Solution

* py

  ```py
  from bisect import bisect_left, bisect_right
  class MajorityChecker(object):
    def __init__(self, A):
      a2i = collections.defaultdict(list)
      for i, x in enumerate(A):
        a2i[x].append(i)
      self.A, self.a2i = A, a2i

    def query(self, left, right, threshold):
      for _ in range(20):
        a = self.A[random.randint(left, right)]
        if bisect_right(self.a2i[a], right) - bisect_left(self.a2i[a], left) >= threshold:
          return a
      return -1
  ```
