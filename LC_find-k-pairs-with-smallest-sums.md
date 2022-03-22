{% tabs %}{% tab title='LC_373.py' %}

```py
def kSmallestPairs(self, nums1, nums2, k):
  streams = map(lambda u: ([u + v, u, v] for v in nums2), nums1)
  stream = heapq.merge(*streams)
  return [suv[1:] for suv in islice(stream, k)]
```

{% endtab %}{% endtabs %}