# [LC_range-module](https://leetcode.com/problems/range-module)

* en

  ```en
  A Range Module is a module that tracks ranges of numbers, implement the following interfaces
    addRange(int left, int right)
    queryRange(int left, int right)
    removeRange(int left, int right)
  ```

* tc

  ```tc
  addRange(10, 20): null
  removeRange(14, 16): null
  queryRange(10, 14): true (Every number in [10, 14) is being tracked)
  queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
  queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
  ```

## Solution

* py

  ```py
  from bisect import bisect_left, bisect_right

  class RangeModule:

    def __init__(self):
      self._X = []

    def addRange(self, left, right):
      i, j = bisect_left(self._X, left), bisect_right(self._X, right)
      self._X[i:j] = [left] * (i % 2 == 0) + [right] * (j % 2 == 0)

    def queryRange(self, left, right):
      i, j = bisect_right(self._X, left), bisect_left(self._X, right)
      return i == j and i%2 == 1

    def removeRange(self, left, right):
      i, j = bisect_left(self._X, left), bisect_right(self._X, right)
      self._X[i:j] = [left]*(i % 2 == 1) + [right] * (j % 2 == 1)
  ```
