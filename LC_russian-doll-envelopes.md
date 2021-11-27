{% tabs %}{% tab title='LC_354.py' %}

```py
def maxEnvelopes(self, en: List[List[int]]) -> int:
  en.sort(key = lambda x: (x[0], -x[1]))
  nums, lis = [j for _, j in en], []
  for current in nums:
    idx = bisect.bisect_left(lis, current)
    lis[idx:idx+1] = [current]
  return len(lis)
```

{% endtab %}{% endtabs %}
