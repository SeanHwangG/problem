# [LC_concatenated-words](https://leetcode.com/problems/concatenated-words)

```en
Given array of unique strings words, return all the concatenated words in the given list of words
```

```txt
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
```

## Solution

* py

  ```py
  def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    words = set(words)
    @lru_cache(None)
    def dfs(word):
      for i in range(1, len(word)):
        prefix, suffix = word[:i], word[i:]
        if prefix in words and (suffix in words or dfs(suffix)):
          return True
      return False
    return [word for word in words if dfs(word)]
  ```
