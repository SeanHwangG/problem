```py
class WordFilter:
  def __init__(self, words):
    self.dic = {}
    for weight, word in enumerate(words):
      for i in range(len(word) + 1):
        for j in range(len(word) + 1):
          self.dic[word[:i] + "#" + word[j:]] = weight


  def f(self, prefix, suffix):
    return self.dic.get(prefix + '#' + suffix, -1)
```
