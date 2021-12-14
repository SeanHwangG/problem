{% tabs %}{% tab title='LC_35.py' %}

```py
def searchInsert(self, nums, target):
  return bisect.bisect_left(nums, target)
```

{% endtab %}{% endtabs %}
