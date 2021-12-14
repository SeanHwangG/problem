{% tabs %}{% tab title='LC_729.py' %}

```py
class MyCalendar:
  def __init__(self):
    self.intervals = []

  def book(self, start : int, end : int) -> bool:
    i = bisect.bisect_right(self.intervals, start)
    j = bisect.bisect_left(self.intervals, end)
    if i % 2 or i != j:  # start is in interval or another interval exists
      return False

    self.intervals[i:i] = [start, end]
    return True
```

{% endtab %}{% endtabs %}
