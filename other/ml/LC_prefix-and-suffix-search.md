# [LC_prefix-and-suffix-search](https://leetcode.com/problems/prefix-and-suffix-search)

```en
Implement the WordFilter class:
WordFilter(string[] words): Initializes the object with the words in the dictionary.
f(string prefix, string suffix): Returns index of the word in the dictionary, which has prefix and suffix
If there is more than one valid index, return the largest of them, -1 if there is no such word
```

```txt
Input:
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]

Output: [null, 0]
```

## Solution

* py

  ```py
  class WordFilter:
    def __init__(self, words):
      self.dic = {}
      for weight, word in enumerate(words):
        for i in range(len(word) + 1):
          for j in range(len(word) + 1):
            self.dic[word[:i] + "#" + word[j:]] = weight


    def f(self, prefix, suffix):
      return self.dic.get(prefix + '#' + suffix, -1)
  ```
