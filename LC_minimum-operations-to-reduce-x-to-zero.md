{% tabs %}{% tab title='LC_1658.py' %}

* Equivalent of finding largest contiguous subarrays with sum(nums) - x

```py
def minOperations(self, nums, x) :
  cumsum = [0] + list(accumulate(nums))
  dic = {c : i for i, c in enumerate(cumsum)}
  goal = cumsum[-1] - x
  ans = -float("inf")

  if goal < 0: return -1
  for num in dic:
    if num + goal in dic:
      ans = max(ans, dic[num + goal] - dic[num])

  return len(nums) - ans if ans != -float("inf") else -1
```

{% endtab %}{% endtabs %}