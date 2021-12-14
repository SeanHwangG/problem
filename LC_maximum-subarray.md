{% tabs %}{% tab title='LC_53.py' %}

* Run; O(N)

```py
def maxSubArray(self, nums: List[int]) -> int:
  for i in range(1, len(nums)):
    if nums[i - 1] > 0:
      nums[i] += nums[i - 1]
    return max(nums)
```

{% endtab %}{% endtabs %}
