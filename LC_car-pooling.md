{% tabs %}{% tab title='LC_1094.py' %}

```py
def carPooling(self, trips, capacity):
  for i, v in sorted(x for n, i, j in trips for x in [[i, n], [j, - n]]):
    capacity -= v
    if capacity < 0:
      return False
  return True
```

{% endtab %}{% endtabs %}