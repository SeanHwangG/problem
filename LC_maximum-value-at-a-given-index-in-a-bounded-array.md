{% tabs %}{% tab title='LC_1802.py' %}

```py
def maxValue(self, n, index, maxSum):
  def test(mid):
    left = max(mid - index, 0)
    right = max(mid - ((n - 1) - index), 0)
    return (mid + left) * (mid - left + 1) // 2 + (mid + right - 1) * (mid - right) // 2

  maxSum -= n
  left, right = 0, maxSum
  while left < right:
    mid = (left + right + 1) // 2
    if test(mid) <= maxSum:
      left = mid
    else:
      right = mid - 1
  return left + 1
```

{% endtab %}{% endtabs %}
