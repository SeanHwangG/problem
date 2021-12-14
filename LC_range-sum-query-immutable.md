{% tabs %}{% tab title='LC_303.py' %}

```py
class NumArray:
  def __init__(self, nums: List[int]):
    summ = 0
    self.prefix = [summ := summ + num for num in nums]

  def sumRange(self, i: int, j: int) -> int:
    return self.prefix[j] - (self.prefix[i - 1] if i > 0 else 0)
```

{% endtab %}{% endtabs %}
