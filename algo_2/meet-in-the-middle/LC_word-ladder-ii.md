# [LC_word-ladder-ii](https://leetcode.com/problems/word-ladder-ii)

* en

  ```en
  Transformation sequence from word begin to word end using dictionary wordList is words[] begin, s1, ..., sk ST
    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that begin does not need to be in wordList.
    sk == end
  Given two words (begin, end), dictionary wordList, return all shortest transformation sequences from begin to end
  Each sequence should be returned as a list of the words [begin, s1, s2, ..., sk].
  ```

* tc

  ```tc
  Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
  Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
  ```

## Solution

* py

  ```py
  def findLadders(self, begin: str, end: str, words: List[str]) -> List[List[str]]:
    def construct_tree(begin, end):
      if begin == end:
        return [[begin]]
      return [[begin] + path for nei in tree[begin] for path in construct_tree(nei, end)]
    def add_path(word, nei, forward):
      if forward:
        tree[word].append(nei)
      else:
        tree[nei].append(word)
      return nei
    words, front, back, forward, tree = set(words), set([begin]), set([end]), True, defaultdict(list)
    if end not in words:
      return []
    while front:
      words -= front
      front = set(add_path(w, w[:i] + ch + w[i + 1:], forward) for w in front for i in range(len(w)) for ch in ascii_lowercase
        if w[:i] + ch + w[i + 1:] in words)
      if front & back:
        break
      if len(front) > len(back):
        front, back, forward = back, front, not forward
    return construct_tree(begin, end)
  ```
