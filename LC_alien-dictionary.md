{% tabs %}{% tab title='LC_269.py' %}

```py
def alienOrder(self, words):
  pre, suc = defaultdict(set), defaultdict(set)
  for pair in zip(words, words[1:]):
    for a, b in zip(*pair):
      if a != b:
        suc[a].add(b)
        pre[b].add(a)
        break
    else:
      if len(pair[0]) > len(pair[1]):
        return ''
  chars, order = set(''.join(words)), []
  free = chars - set(pre)
  while free:
    a = free.pop()
    order.append(a)
    for b in suc[a]:
      pre[b].discard(a)
      if not pre[b]:
        free.add(b)
  return ''.join(order) * (set(order) == chars)
```

{% endtab %}{% endtabs %}
