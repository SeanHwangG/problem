{% tabs %}{% tab title='LC_268.py' %}

```py
def missingNumber(self, nums: List[int]) -> int:
  n = len(nums)
  return n * (n+1) // 2 - sum(nums)
```

{% endtab %}{% endtabs %}
