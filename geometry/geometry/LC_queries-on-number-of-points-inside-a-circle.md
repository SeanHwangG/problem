# [LC_queries-on-number-of-points-inside-a-circle](https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle)

* en

  ```en
  oints where points[i] = [xi, yi] is coordinates of ith point on a 2D plane. 2+ points can have same coordinates
  queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj
  For each query queries[j], compute number of points inside jth circle including on border
  Return array answer, where answer[j] is answer to the jth query
  ```

* tc

  ```tc
  Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
  Output: [3,2,2]
  ```

## Solution

* py

  ```py
  def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
    points.sort()
    result = [0] * len(queries)
    for ii, (qx, qy, qr) in enumerate(queries):
      lo = bisect_left([p[0] for p in points], qx - qr)
      for jj in range(lo, len(points)):
        px, py = points[jj]
        if px > qx + qr:
          break
        if (qx - px) ** 2 + (qy - py) ** 2 <= qr ** 2:
          result[ii] += 1
    return result
  ```
