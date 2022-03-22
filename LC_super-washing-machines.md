{% tabs %}{% tab title='LC_517.py' %}

```py
def findMinMoves(self, machines):
  total, n = sum(machines), len(machines)
  if total % n: return -1
  target, res, toRight = total / n, 0, 0
  for m in machines:
    toRight = m + toRight - target
    res = max(res, abs(toRight), m - target)
  return res
```

{% endtab %}{% endtabs %}