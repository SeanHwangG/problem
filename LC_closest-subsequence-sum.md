{% tabs %}{% tab title='LC_1755.py' %}

```py
def minAbsDifference(self, nums: List[int], goal: int) -> int:
  def generate_sum(nums):
    ans = {0}
    for x in nums:
      ans |= {x + y for y in ans}
    return ans

  evens = [-inf, *sorted(generate_sum(nums[::2])), inf]

  return min(abs(y + x - goal)
              for x in generate_sum(nums[1::2])
              for k in [bisect_left(evens, goal - x)]
              for y in evens[k - 1 : k + 1])
```

{% endtab %}{% endtabs %}
