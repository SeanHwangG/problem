{% tabs %}{% tab title='LC_581.py' %}

```py
def findUnsortedSubarray(self, nums):
  start, end = -1, 0
  left_prev, right_prev = nums[0], nums[start]

  for i in range(1, len(nums)):
    # find largest index not in place
    if nums[i] < left_prev:
      end = i
    else:
      left_prev = nums[i]

    # find smallest index not in place
    if right_prev < nums[~i]:
      start = ~i
    else:
      right_prev = nums[~i]

  return 0 if end == 0 else end - (len(nums) + start) + 1
```

{% endtab %}{% endtabs %}
