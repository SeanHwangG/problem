{% tabs %}{% tab title='LC_1964.py' %}

```py
def longestObstacleCourseAtEachPosition(self, A):
  mono, res = [], []
  for a in A:
    i = bisect.bisect(mono, a)
    res.append(i + 1)
    if i == len(mono):
      mono.append(0)
    mono[i] = a
  return res
```

{% endtab %}{% endtabs %}
