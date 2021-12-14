{% tabs %}{% tab title='LC_348.py' %}

```py
class TicTacToe(object):
  def __init__(self, n):
    self.n, self.count = n, collections.Counter()

  def move(self, row, col, player):
    for i, x in enumerate((row, col, row+col, row-col)):
      self.count[i, x, player] += 1
      if self.count[i, x, player] == self.n:
        return player
    return 0
```

{% endtab %}{% endtabs %}
