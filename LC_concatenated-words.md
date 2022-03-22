{% tabs %}{% tab title='LC_472.py' %}

```py
def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
  words = set(words)
  @lru_cache(None)
  def dfs(word):
    for i in range(1, len(word)):
      prefix, suffix = word[:i], word[i:]
      if prefix in words and (suffix in words or dfs(suffix)):
        return True
    return False
  return [word for word in words if dfs(word)]
```

{% endtab %}{% endtabs %}