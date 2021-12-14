{% tabs %}{% tab title='LC_1752.py' %}

```py
def check(self, nums: List[int]) -> bool:
  return sum(nums[i] < nums[i-1] for i in range(len(nums))) <= 1
```

{% endtab %}{% endtabs %}
