# [LC_word-squares](https://leetcode.com/problems/word-squares)

```en
Given array of unique strings words, return all the word squares you can build from words in any order
Same word from words can be used multiple times
Sequence of strings forms valid word square if kth row and column read same string, where 0 <= k < max(numRows, numColumns)
```

```txt
Input: words = ["area","lead","wall","lady","ball"]
Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]

Input: words = ["abat","baba","atan","atal"]
Output: [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]
```

## Solution

* py

  ```py
  def wordSquares(self, words: List[str]) -> List[List[str]]:
    n = len(words[0])
    fulls = collections.defaultdict(list)
    for word in words:
      for i in range(n):
        fulls[word[:i]].append(word)
    def build(square):
      if len(square) == n:
        squares.append(square)
        return
      for word in fulls[''.join(list(zip(*square))[len(square)])]:
        build(square + [word])
    squares = []
    for word in words:
      build([word])
    return squares
  ```
