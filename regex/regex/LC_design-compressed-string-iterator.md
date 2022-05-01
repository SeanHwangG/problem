# [LC_design-compressed-string-iterator](https://leetcode.com/problems/design-compressed-string-iterator)

next() Return next character if the original string still has uncompressed characters, otherwise returns white space
hasNext() Return if there is any letter needs to be uncompressed in the original string

```txt
Input:
["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
[["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]

Output:
[null, "L", "e", "e", "t", "C", "o", true, "d", true]
```

## Solution

* py

  ```py
  import re
  class StringIterator(object):
    def __init__(self, compressedString):
      self.tokens = []
      for token in re.findall('\D\d+', compressedString):
        self.tokens.append((token[0], int(token[1:])))
      self.tokens = self.tokens[::-1]

    def next(self):
      if not self.tokens: return ' '
      t, n = self.tokens.pop()
      if n > 1:
        self.tokens.append((t, n - 1))
      return t

    def hasNext(self):
      return bool(self.tokens)
  ```
