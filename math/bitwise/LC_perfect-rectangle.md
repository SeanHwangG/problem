# [LC_perfect-rectangle](https://leetcode.com/problems/perfect-rectangle)

* en

  ```en
  Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle
  Return true if all the rectangles together form an exact cover of a rectangular region
  ```

* tc

  ```tc
  Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
  Output: true  # All 5 rectangles together form an exact cover of a rectangular region.
  ```

## Solution

* py

  ```py
  def isRectangleCover(self, rectangles):
    cornera = set()
    a, b, c, d, area = float('inf'), float('inf'), float('-inf'), float('-inf'), 0
    for x1, y1, x2, y2 in rectangles:
      a, b = min((a, b), (x1, y1))
      c, d = max((c, d), (x2, y2))
      area += (x2-x1) * (y2-y1)
      corner ^= {(x1,y1), (x2,y2), (x1,y2), (x2,y1)}
    return corner == {(a,b), (c,d), (a,d), (c,b)} and area == (c-a) * (d-b)
  ```
