{% tabs %}{% tab title='LC_821.py' %}

```py
def shortestToChar(self, S: str, C: str) -> List[int]:
  ret = [0 if s == C else len(S) for s in S]
  for i in range(1, len(S)):
    ret[i] = min(ret[i - 1] + 1, ret[i])
  for i in range(len(S) - 2, -1, -1):
    ret[i] = min(ret[i + 1] + 1, ret[i])
  return ret
```

{% endtab %}{% endtabs %}
