{% tabs %}{% tab title='LC_528.py' %}

```py
from bisect import bisect_left

def __init__(self, w: List[int]):
  self.numbers = []
  total, count = sum(w), 0
  count = 0
  for index, value in enumerate(w):
    count += value
    self.numbers.append(count / total)

def pickIndex(self) -> int:
    return bisect_left(self.numbers, random.random(), 0, len(self.numbers) - 1)
```

{% endtab %}{% endtabs %}
