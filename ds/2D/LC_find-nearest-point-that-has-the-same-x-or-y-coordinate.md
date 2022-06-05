# [LC_find-nearest-point-that-has-the-same-x-or-y-coordinate](https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate)

```en
Given 2 integers, x and y, which represent your current location on a Cartesian grid: (x, y)
Given array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi)
A point is valid if it shares the same x-coordinate or the same y-coordinate as your location
Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location
```

```txt
Input: x = 3, y = 4,
points =
[[1,2],
 [3,1],
 [2,4],
 [2,3],
 [4,4]]

Output: 2
```

## Solution

* py

  ```py
  def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
    distances = [abs(x - p[0]) + abs(y - p[1]) if p[0] == x or p[1] == y else float('inf') for p in points]
    return distances.index(min(distances)) if min(distances) != float('inf') else -1
  ```
