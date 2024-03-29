# [LC_data-stream-as-disjoint-intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals)

* en

  ```en
  Given data stream input of non-negative integers a1, ..., an, summarize the numbers seen as a list of intervals
    SummaryRanges(): Initializes the object with an empty stream
    void addNum(int val): Adds the integer val to the stream
    int[][] getIntervals(): Return summary of ints in stream currently as list of disjoint intervals [starti, endi]
  ```

* tc

  ```tc
  Input:
  ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals",\
  "addNum", "getIntervals"]
  [[], [1], [], [3], [], [7], [], [2], [], [6], []]

  Output:
  [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3],\
  [6, 7]]]
  ```

## Solution

* py

  ```py
  class SummaryRanges:
    def __init__(self):
      self.intervals = [[float('-inf'), float('-inf')], [float('inf'), float('inf')]]

    def addNum(self, val: int) -> None:
      i = bisect.bisect(self.intervals, [val])
      (ps, pe), (ns, ne) = self.intervals[i - 1], self.intervals[i]

      if pe == val - 1 and ns == val + 1:  # merge with left, right
        self.intervals = self.intervals[:i - 1] + [[ps, ne]] + self.intervals[i + 1:]
      elif pe == val - 1:                  # merge with left
        self.intervals[i - 1][1] = val
      elif ns == val + 1:                  # merge with right
        self.intervals[i][0] = val
      elif pe < val - 1 and ns > val + 1:
        self.intervals = self.intervals[:i] + [[val, val]] + self.intervals[i:]

    def getIntervals(self) -> List[List[int]]:
      return self.intervals[1:-1]
  ```
