{% tabs %}{% tab title='LC_567.py' %}

```py
def checkInclusion(self, s1: str, s2: str) -> bool:
  k = len(s1)
  d1, d2 = Counter(s1), Counter(s2[:k])
  if d1 == d2:
    return True

  for i in range(len(s2) - k):
    if d2[s2[i]] == 1:
      del d2[s2[i]]
    elif d2[s2[i]] > 1:
      d2[s2[i]] -= 1
    d2[s2[i + k]] += 1
    if d1 == d2:
      return True

  return False
```

{% endtab %}{% endtabs %}
