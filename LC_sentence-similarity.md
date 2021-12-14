{% tabs %}{% tab title='LC_734.py' %}

```py
def areSentencesSimilar(self, A: List[str], B: List[str], pairs: List[List[str]]) -> bool:
  l1, l2, pairs = len(A), len(B), {(p1, p2) for p1, p2 in pairs}
  if l1 != l2: return False
  return not any((w1, w2) not in pairs and (w2, w1) not in pairs and w1 != w2 for w1, w2 in zip(A, B))
```

{% tab title='LC_734.js' %}
{% endtab %}

```js
var areSentencesSimilar = function(words1, words2, pairs) {
  if (words1.length !== words2.length) return false;
  const dict = pairs.reduce((set, pair) => set.add(`${pair[0]}${pair[1]}`), new Set);
  return words1.every((w, i) => w === words2[i] || dict.has(`${w}${words2[i]}`) || dict.has(`${words2[i]}${w}`))
};
```

{% endtab %}{% endtabs %}
