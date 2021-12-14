{% tabs %}{% tab title='LC_757.py' %}

```py
def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
  intervals.sort(key=lambda x:(x[1],-x[0]))
  res = 0
  cur = []
  for start, end in intervals:
    if not cur or start > cur[1]:
      res += 2
      cur = [end - 1, end]
    elif start > cur[0]:
      res += 1
      cur = [cur[1], end]
  return res
```

{% endtab %}{% endtabs %}
