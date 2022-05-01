# [LC_check-if-it-is-a-straight-line](https://leetcode.com/problems/check-if-it-is-a-straight-line)

Given an array coordinates, coordinates[i] = [x, y], where [x, y] represents coordinate of a point
Check if these points make a straight line in the XY plane.

```txt
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
```

## Solution

* Time: O(N)
* Space: O(1)

* py

  ```py
  def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    (x0, y0), (x1, y1) = coordinates[: 2]
    return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)
  ```
