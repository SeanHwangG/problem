{% tabs %}{% tab title='LC_1244.py' %}

```py
class Leaderboard(object):
  def __init__(self):
    self.A = collections.Counter()

  def addScore(self, playerId, score):
    self.A[playerId] += score

  def top(self, K):
    return sum(v for i,v in self.A.most_common(K))

  def reset(self, playerId):
    self.A[playerId] = 0
```

{% endtab %}{% endtabs %}
