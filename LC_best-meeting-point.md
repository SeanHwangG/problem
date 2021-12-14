{% tabs %}{% tab title='LC_296.py' %}

* Median of all ones

```py
def minTotalDistance(self, grid: List[List[int]]) -> int:
  total = 0
  for grid in grid, zip(*grid):
    X = []
    for x, row in enumerate(grid):
      X += [x] * sum(row)
    total += sum(abs(x - X[len(X) // 2]) for x in X)
  return total
```

{% endtab %}{% endtabs %}
