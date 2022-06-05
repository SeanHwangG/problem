# [LC_set-intersection-size-at-least-two](https://leetcode.com/problems/set-intersection-size-at-least-two)

```en
Int interval [a, b] (for integers a < b) is a set of all consecutive integers from a to b, including a, b
Find min size of a set S st for every integer interval A in intervals, intersection of S with A has size 2+
```

```txt
Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
Output: 3 # {2, 3 4}
```

## Solution

* py

  ```py
  def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x:(x[1],-x[0]))
    res = 0
    cur = []
    for start, end in intervals:
      if not cur or start > cur[1]:
        res += 2
        cur = [end - 1, end]
      elif start > cur[0]:
        res += 1
        cur = [cur[1], end]
    return res
  ```
