{% tabs %}{% tab title='LC_759.py' %}

```py
def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
  iterator = merge(*schedule, key=operator.attrgetter('start'))
  res, prev_end = [], next(iterator).end
  for event in iterator:
    if event.start > prev_end:
      res.append(Interval(prev_end, event.start))
    prev_end = max(prev_end, event.end)
  return res
```

{% endtab %}{% endtabs %}
