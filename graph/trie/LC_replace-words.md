# [LC_replace-words](https://leetcode.com/problems/replace-words)

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces
Replace all successors in sentence with root forming it
If successor can be replaced by more than one root, replace it with the root that has the shortest length

```txt
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```

## Solution

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
