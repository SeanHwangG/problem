{% tabs %}{% tab title='LC_1791.py' %}

```py
def findCenter(self, edges: List[List[int]]) -> int:
  return collections.Counter([v for edge in edges for v in edge]).most_common()[0][0]
```

{% endtab %}{% endtabs %}
