{% tabs %}{% tab title='LC_55.py' %}

```py
def canJump(self, nums: List[int]) -> bool:
  pos = 0
  for i, n in enumerate(nums):
    if i <= pos:
      pos = max(pos, i + n)
  return len(nums) - 1 <= pos
```

{% endtab %}{% endtabs %}
