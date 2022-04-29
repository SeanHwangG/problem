# [LC_alien-dictionary](https://leetcode.com/problems/alien-dictionary)

There is new alien language that uses English alphabet. However, order among letters is unknown to you
Given list of words from alien language's dictionary, with sorted string by rule of this new language

```txt
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Input: words = ["z","x","z"]
Output: ""  # The order is invalid, so return "".
```

## Solution

* py

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
