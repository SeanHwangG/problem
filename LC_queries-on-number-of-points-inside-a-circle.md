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
