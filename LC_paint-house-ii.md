{% tabs %}{% tab title='LC_265.py' %}

* Time; O(NK)

```py
def minCostII(self, costs: List[List[int]]) -> int:
  return min(reduce(lambda x, y: self.combine(y, x), costs)) if costs else 0

def combine(self, house, tmp):
  m, n, i = min(tmp), len(tmp), tmp.index(min(tmp))
  tmp = [m] * i + [min(tmp[0: i] + tmp[i + 1:])] + [m] * (n - i - 1)
  return [sum(i) for i in zip(house, tmp)]
```

{% endtab %}{% endtabs %}
