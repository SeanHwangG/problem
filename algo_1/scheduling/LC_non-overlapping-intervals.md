# [LC_non-overlapping-intervals](https://leetcode.com/problems/non-overlapping-intervals)

* en

  ```en
  Given array of intervals intervals where intervals[i] = [starti, endi]
  Return min number of intervals you need to remove to make the rest of the intervals non-overlapping
  ```

* tc

  ```tc
  Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
  Output: 1
  ```

## Solution

* py

  ```py
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    end, cnt = float('-inf'), 0
    for s, e in sorted(intervals, key=lambda x: x[1]):
      if s >= end:
        end = e
      else:
        cnt += 1
    return cnt
  ```
