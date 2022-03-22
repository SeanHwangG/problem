{% tabs %}{% tab title='LC_1232.py' %}

* Time: O(N)
* Space: O(1)

```py
def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
  (x0, y0), (x1, y1) = coordinates[: 2]
  return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)
```

{% endtab %}{% endtabs %}