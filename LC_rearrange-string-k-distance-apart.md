{% tabs %}{% tab title='LC_358.py' %}

```py
def rearrangeString(self, s: str, k: int) -> str:
  n = len(s)
  if not k:
    return s
  count = Counter(s)
  maxf = max(count.values())
  if (maxf - 1) * k + list(count.values()).count(maxf) > len(s):
    return ""
  res, i = list(s), (n - 1) % k
  for c in sorted(count, key = lambda i: -count[i]):
    for j in range(count[c]):
      res[i] = c
      i += k
      if i >= n:
        i = (i - 1) % k
  return "".join(res)
```

{% endtab %}{% endtabs %}
