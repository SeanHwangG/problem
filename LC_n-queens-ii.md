{% tabs %}{% tab title='LC_52.py' %}

```py
def totalNQueens(self, n: int, queens=[], d1=[], d2=[]) -> int:
  i = len(queens)
  return (i == n) + sum(self.totalNQueens(n, queens+[j], d1+[j-i], d2+[j+i]) for j in range(n) \
              if j not in queens and j - i not in d1 and j + i not in d2)
```

{% endtab %}{% endtabs %}
