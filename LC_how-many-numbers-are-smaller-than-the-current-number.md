{% tabs %}{% tab title='LC_1365.py' %}

```py
def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
  return [sum(m < n for m in nums) for n in nums]
```

{% endtab %}{% endtabs %}
