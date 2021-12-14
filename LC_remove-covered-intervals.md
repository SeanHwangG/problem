{% tabs %}{% tab title='LC_1288.py' %}

```py
def removeCoveredIntervals(self, A: List[List[int]]) -> int:
  res = right = 0
  A.sort(key=lambda a: (a[0], -a[1]))
  for i, j in A:
    res += j > right
    right = max(right, j)
  return res
```

{% endtab %}{% endtabs %}
