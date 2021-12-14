{% tabs %}{% tab title='LC_126.py' %}

```py
def findLadders(self, begin: str, end: str, words: List[str]) -> List[List[str]]:
  def construct_tree(begin, end):
    if begin == end:
      return [[begin]]
    return [[begin] + path for nei in tree[begin] for path in construct_tree(nei, end)]
  def add_path(word, nei, forward):
    if forward:
      tree[word].append(nei)
    else:
      tree[nei].append(word)
    return nei
  words, front, back, forward, tree = set(words), set([begin]), set([end]), True, defaultdict(list)
  if end not in words:
    return []
  while front:
    words -= front
    front = set(add_path(w, w[:i] + ch + w[i + 1:], forward) for w in front for i in range(len(w)) for ch in ascii_lowercase
      if w[:i] + ch + w[i + 1:] in words)
    if front & back:
      break
    if len(front) > len(back):
      front, back, forward = back, front, not forward
  return construct_tree(begin, end)
```

{% endtab %}{% endtabs %}
