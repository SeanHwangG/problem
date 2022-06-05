# [LC_merge-intervals](https://leetcode.com/problems/merge-intervals)

```en
Merge all overlapping intervals, return array of non-overlapping intervals that cover all intervals in input
```

```txt
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

## Solution

* py

  ```py
  def merge(self, intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i[0]):
      if out and i[0] <= out[-1][1]:
        out[-1][1] = max(out[-1][1], i[1])
      else:
        out += [i]
    return out
  ```
