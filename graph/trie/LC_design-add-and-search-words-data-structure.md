# [LC_design-add-and-search-words-data-structure](https://leetcode.com/problems/design-add-and-search-words-data-structure)

* en

  ```en
  Design a data structure that supports adding new words and finding if a string matches any previously added string
  Implement the WordDictionary class:
    WordDictionary() Initializes the object
    void addWord(word) Adds word to the data structure, it can be matched later
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise
      word may contain dots '.' where dots can be matched with any letter
  ```

* tc

  ```tc
  Input
  ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
  [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

  Output
  [null,null,null,null,false,true,true,true]
  ```

## Solution

* py

  ```py
  class WordDictionary:
    def __init__(self):
      self.trie = {}

    def addWord(self, word: str) -> None:
      node = self.trie
      for c in word + "$":
        node = node.setdefault(c, {})

    def search(self, word: str) -> bool:
      return self.searchNode(self.trie, word)

    def searchNode(self, node, word: str) -> bool:
      for i, c in enumerate(word):
        if c == '.':
          return any(self.searchNode(node[w], word[i+1:]) for w in node if w != '$')
        if c not in node:
          return False
        node = node[c]
      return '$' in node
  ```
