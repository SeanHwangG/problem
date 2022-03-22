{% tabs %}{% tab title='LC_211.py' %}

```py
class WordDictionary:
  def __init__(self):
    self.trie = {}

  def addWord(self, word: str) -> None:
    node = self.trie
    for c in word + "$":
      node = node.setdefault(c, {})

  def search(self, word: str) -> bool:
    return self.searchNode(self.trie, word)

  def searchNode(self, node, word: str) -> bool:
    for i, c in enumerate(word):
      if c == '.':
        return any(self.searchNode(node[w], word[i+1:]) for w in node if w != '$')
      if c not in node:
        return False
      node = node[c]
    return '$' in node
```

{% endtab %}{% endtabs %}