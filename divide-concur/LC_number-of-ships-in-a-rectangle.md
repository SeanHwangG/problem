```py
def countShips(self, sea, P, Q):
  res = 0
  if P.x >= Q.x and P.y >= Q.y and sea.hasShips(P, Q):
      if P.x == Q.x and P.y == Q.y: return 1
      mx, my = (P.x + Q.x) // 2, (P.y + Q.y) // 2
      res += self.countShips(sea, P, Point(mx + 1, my + 1))
      res += self.countShips(sea, Point(mx, P.y), Point(Q.x, my + 1))
      res += self.countShips(sea, Point(mx, my), Q)
      res += self.countShips(sea, Point(P.x, my), Point(mx + 1, Q.y))
  return res
```
