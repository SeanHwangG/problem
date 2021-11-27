{% tabs %}{% tab title='LC_249.py' %}

```py
def groupStrings(self, strings):
  key = lambda s: [(ord(c) - ord(s[0])) % 26 for c in s]
  return [list(g) for _, g in itertools.groupby(sorted(strings, key=key), key)]
```

{% endtab %}{% endtabs %}
