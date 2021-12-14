{% tabs %}{% tab title='LC_244.py' %}

* Time; O(m + n)

```py
class WordDistance:
  def __init__(self, words):
    self.dic, self.l = defaultdict(list), len(words)
    for i, x in enumerate(words):
      self.dic[x].append(i)

  def shortest(self, word1, word2):
    l1, l2, res = self.dic[word1], self.dic[word2], self.l
    i = j = 0
    while i < len(l1) and j < len(l2):
      res = min(res, abs(l1[i] - l2[j]))
      if l1[i] < l2[j]:
        i += 1
      else:
        j += 1
    return res
```

{% endtab %}{% endtabs %}
