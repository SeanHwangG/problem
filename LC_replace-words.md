{% tabs %}{% tab title='LC_648.py' %}

* Time; O(N)
* Space; O(N*K)

```py
def replaceWords(self, roots, sentence):
  _trie = lambda: collections.defaultdict(_trie)
  trie = _trie()
  for root in roots:
    cur = trie
    for letter in root:
      cur = cur[letter]
    cur["END"] = root

  def replace(word):
    cur = trie
    for letter in word:
      if letter not in cur: break
      cur = cur[letter]
      if "END" in cur:
        return cur["END"]
    return word

  return " ".join(map(replace, sentence.split()))
```

{% endtab %}{% endtabs %}
