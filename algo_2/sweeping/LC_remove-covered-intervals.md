# [LC_remove-covered-intervals](https://leetcode.com/problems/remove-covered-intervals)

* en

  ```en
  Given list of intervals, remove all intervals that are covered by another interval in the list
  Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d
  ```

* tc

  ```tc
  Input: intervals = [[1,4],[3,6],[2,8]]
  Output: 2
  ```

## Solution

* py

  ```py
  def removeCoveredIntervals(self, A: List[List[int]]) -> int:
    res = right = 0
    A.sort(key=lambda a: (a[0], -a[1]))
    for i, j in A:
      res += j > right
      right = max(right, j)
    return res
  ```
