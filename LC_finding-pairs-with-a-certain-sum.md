{% tabs %}{% tab title='LC_1865.py' %}

```py
class FindSumPairs:
  def __init__(self, nums1: List[int], nums2: List[int]):
    self.c1, c2 = Counter(nums1), Counter(nums2)
    self.l2 = nums2

  def add(self, idx: int, val: int) -> None:
    self.c2[self.l2[idx]] -= 1
    self.l2[idx] += val
    self.c2[self.l2[idx]] += 1

  def count(self, tot: int) -> int:
    return sum(v * self.c2[tot - k] for k, v in self.c1.items())
```

{% endtab %}{% endtabs %}
