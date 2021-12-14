{% tabs %}{% tab title='LC_357.py' %}

```py
def countNumbersWithUniqueDigits(self, n: int) -> int:
  res, prev = 10, 9
  for i in range(1, n):
    prev *= 10 - i
    res += prev
  return n and res or 1
```

{% endtab %}{% endtabs %}
