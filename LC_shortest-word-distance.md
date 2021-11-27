{% tabs %}{% tab title='LC_243.py' %}

```py
def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
  ans, cur_word, cur_idx = len(words), None, 0
  for index, word in enumerate(words):
    if word != word1 and word != word2:
      continue
    if cur_word and word != cur_word:
      ans = min(ans, index - cur_idx)
    cur_word, cur_idx = word, index
  return ans
```

{% endtab %}{% endtabs %}
