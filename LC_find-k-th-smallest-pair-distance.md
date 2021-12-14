{% tabs %}{% tab title='LC_719.py' %}

```py
def smallestDistancePair(self, li: List[int], k: int) -> int:
  def enough(distance) -> bool:  # two pointers
    count, l, r = 0, 0, 0
    while l < len(li) or r < len(li):
      while r < len(li) and li[r] - li[l] <= distance:
        r += 1
      count += r - l - 1
      l += 1
    return count >= k

  li.sort()
  l, r = 0, li[-1] - li[0]
  while l < r:
    m = l + (r - l) // 2
    if not enough(m):
      l = m + 1
    else:
      r = m
  return l
```

{% endtab %}{% endtabs %}
