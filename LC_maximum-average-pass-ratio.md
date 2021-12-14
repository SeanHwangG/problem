{% tabs %}{% tab title='LC_1792.py' %}

```py
def maxAverageRatio(self, A, k):
  h = [(a / b - (a + 1) / (b + 1), a, b) for a, b in A]
  heapify(h)
  for _ in range(k):
    v, a, b = heapq.heappop(h)
    a, b = a + 1, b + 1
    heapq.heappush(h, (-(a + 1) / (b + 1) + a / b, a, b))
  return sum(a / b for v, a, b in h) / len(h)
```

{% endtab %}{% endtabs %}
