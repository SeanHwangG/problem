# [LC_design-search-autocomplete-system](https://leetcode.com/problems/design-search-autocomplete-system)

* en

  ```en
  Users may input a sentence (at least one word and end with a special character '#').
  Given a string array sentences and an integer array times both of length n
  Sentences[i] is a previously typed sentence and times[i] is the corresponding number of times sentence was typed
  For each input character except #, return top 3 hot sentences that have same prefix as part of sentence already typed
  ```

* tc

  ```tc
  Input:
  ["AutocompleteSystem", "input", "input", "input", "input"]
  [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]

  Output:
  [null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]
  ```

## Solution

* py

  ```py
  _trie = lambda: collections.defaultdict(_trie)

  class ShortList(list):  # Keep track of only the top 3 answers
    def append(self, val):
      for i, (nt, s) in enumerate(self):
        if s == val[1]:
          self[i] = val
          break
      else:
        list.append(self, val)
      self.sort()
      if len(self) > 3:
        self.pop()

  class AutocompleteSystem:
    def __init__(self, sentences, counts):
      self.curnode = self.trie = _trie()
      self.sentence_to_count, self.search = collections.Counter(), ''

      for sentence, count in zip(sentences, counts):
        self.add(sentence, count)

    def add(self, sentence, count):
      self.sentence_to_count[sentence] = count
      cur = self.trie
      self._add_info(cur, sentence, count)
      for letter in sentence:
        cur = cur[letter]
        self._add_info(cur, sentence, count)
      cur["END"] = sentence

    def _add_info(self, node, sentence, count):
      if "INFO" not in node:
        node["INFO"] = ShortList()
      node["INFO"].append((-count, sentence))

    def input(self, c):
      if c != '#':
        self.search += c
        if self.curnode is None:
          return []
        if c not in self.curnode:
          self.curnode = None
          return []

        self.curnode = self.curnode[c]
        return [s for nt, s in self.curnode["INFO"]]
      else:
        self.sentence_to_count[self.search] += 1
        self.add(self.search, self.sentence_to_count[self.search])
        self.search, self.curnode = '', self.trie
        return []
  ```
