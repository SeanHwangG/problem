{% tabs %}{% tab title='LC_1815.py' %}

* Time: O((n/K)^K * K)
* Space: O((n/K)^K * K)

```py
def maxHappyGroups(self, batch_size: int, groups: List[int]) -> int:
  @lru_cache(None)
  def dp(remains: tuple, waiting: int) -> int:
    ans = 0
    for i in range(batch_size):
      if remains[i] > 0:
        next_remains = tuple(remain - int(i == j) for j, remain in enumerate(remains))
        rest = (waiting + i) % batch_size
        ans = max(ans, dp(next_remains, rest) + (waiting == 0))
    return ans

  remains = [0] * batch_size
  for group in groups:
    remains[group % batch_size] += 1
  ans, remains[0] = remains[0], 0
  for i in range(1, batch_size):
    happy = min(remains[i], remains[batch_size-i])
    if i == batch_size - i:
      happy = remains[i] // 2
    ans += happy
    remains[i] -= happy
    remains[batch_size - i] -= happy
  return ans + dp(tuple(remains), 0)
```

{% endtab %}{% endtabs %}
