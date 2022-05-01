# [LC_implement-trie-prefix-tree](https://leetcode.com/problems/implement-trie-prefix-tree)

Design Trie

```txt
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output:
[null, null, true, false, true, null, true]
```

## Solution

* cpp

  ```cpp
  class Trie {
  public:
    Trie() {}

    void insert(string word) {
      Trie* node = this;
      for (char ch : word) {
        if (!node->next.count(ch)) node->next[ch] = new Trie();
        node = node->next[ch];
      }
      node->isword = true;
    }

    bool search(string word) {
      Trie* node = this;
      for (char ch : word) {
        if (!node->next.count(ch)) return false;
        node = node->next[ch];
      }
      return node->isword;
    }

    bool startsWith(string prefix) {
      Trie* node = this;
      for (char ch : prefix) {
        if (!node->next.count(ch)) return false;
        node = node->next[ch];
      }
      return true;
    }

  private:
    map<char, Trie*> next = {};
    bool isword = false;
  };
  ```

* py

  ```py
  class Trie:
    def __init__(self):
      T = lambda: collections.defaultdict(T)
      self.root = T()

    def insert(self, word):
      reduce(dict.__getitem__, word, self.root)['#'] = True

    def search(self, word):
      return '#' in reduce(lambda cur, c: cur.get(c, {}), word, self.root)

    def startsWith(self, prefix):
      return bool(reduce(lambda cur, c: cur.get(c, {}), prefix, self.root))
  ```
