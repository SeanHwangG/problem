{% tabs %}{% tab title='LC_560.py' %}

```py
def subarraySum(self, nums: List[int], k: int) -> int:
  count, cur, res = {0: 1}, 0, 0
  for v in nums:
    cur += v
    res += count.get(cur - k, 0)
    count[cur] = count.get(cur, 0) + 1
  return res
```

{% endtab %}{% endtabs %}