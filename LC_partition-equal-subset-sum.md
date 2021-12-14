{% tabs %}{% tab title='LC_416.py' %}

```py
def canPartition(nums):
  if sum(nums) & 1 == 0:
    target = sum(nums) >> 1
    dp = {0}
    for i in nums:
      dp |= {i + x for x in dp}
      if target in dp:
        return True
  return False
```

{% endtab %}{% endtabs %}
