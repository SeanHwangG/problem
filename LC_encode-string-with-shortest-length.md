{% tabs %}{% tab title='LC_471.py' %}

```py
@lru_cache(None)
def encode(self, s: str) -> str:
  n = len(s)
  i = (s + s).find(s, 1)
  one = f'{n // i}[{self.encode(s[:i])}]' if i < n else s
  multi = [self.encode(s[:i]) + self.encode(s[i:]) for i in range(1, n)]
  return min([s, one] + multi, key=len)
```

{% endtab %}{% endtabs %}
