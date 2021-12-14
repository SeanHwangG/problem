{% tabs %}{% tab title='LC_1046.js' %}

```js
const lastStoneWeight = s =>
  1 === s.length ? s[0] : lastStoneWeight(s.sort((a, b) => a - b).concat(s.pop() - s.pop()));
```

{% endtab %}{% tab title='LC_1046.py' %}

```py
def lastStoneWeight(self, l: List[int]) -> int:
  l = [-e for e in l]
  heapq.heapify(l)
  while len(l) > 1:
    mx1 = heapq.heappop(l)
    mx2 = heapq.heappop(l)
    if mx1 != mx2:
      heapq.heappush(l, mx1 - mx2)
  return 0 if len(l) == 0 else -l[0]
```

{% endtab %}{% endtabs %}
