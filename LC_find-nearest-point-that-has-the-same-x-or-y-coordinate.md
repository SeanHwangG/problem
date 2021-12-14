{% tabs %}{% tab title='LC_1779.py' %}

```py
def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
  distances = [abs(x - p[0]) + abs(y - p[1]) if p[0] == x or p[1] == y else float('inf') for p in points]
  return distances.index(min(distances)) if min(distances) != float('inf') else -1
```

{% endtab %}{% endtabs %}
