{% tabs %}{% tab title='LC_332.py' %}

```py
def findItinerary(self, tickets: List[List[str]]) -> List[str]:
  targets = collections.defaultdict(list)
  for a, b in sorted(tickets)[::-1]:
    targets[a] += b,
  route, stk = [], ['JFK']
  while stk:
    while targets[stk[-1]]:
      stk += [targets[stk[-1]].pop()]
    route += [stk.pop()]
  return route[::-1]
```

{% endtab %}{% endtabs %}
