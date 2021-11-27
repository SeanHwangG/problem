{% tabs %}{% tab title='LC_1274.md' %}

* Given Sea.hasShips(topRight, bottomLeft) which returns if at least one ship in the rectangle represented by 2 points
* Given two points: top right, bottom left corners of a rectangle, return # ships present in that rectangle

```txt
ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
Output: 3

Input: ans = [[1,1],[2,2],[3,3]], topRight = [1000,1000], bottomLeft = [0,0]
Output: 3
```

{% endtab %}{% tab title='LC_1274.py' %}

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

{% endtab %}{% endtabs %}
