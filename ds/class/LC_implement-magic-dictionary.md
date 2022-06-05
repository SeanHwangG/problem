# [LC_implement-magic-dictionary](https://leetcode.com/problems/implement-magic-dictionary)

```en
Implement the MagicDictionary class:
  MagicDictionary() Initializes the object
  void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary
  bool search(String searchWord) Return if change exactly 1 character in searchWord to match any string in data structure
```

```txt
Input:
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]

Output: [null, null, false, true, false, false]
```

## Solution

* py

  ```py
  class MagicDictionary:
    def _candidates(self, word):
      for i in range(len(word)):
        yield word[:i] + '*' + word[i+1:]

    def buildDict(self, words):
      self.words = set(words)
      self.near = collections.Counter(cand for word in words for cand in self._candidates(word))

    def search(self, word):
      return any(self.near[cand] > 1 or self.near[cand] == 1 and word not in self.words for cand in self._candidates(word))
  ```
