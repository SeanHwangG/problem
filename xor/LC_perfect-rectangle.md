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
