# [LC_find-the-shortest-superstring](https://leetcode.com/problems/find-the-shortest-superstring)

* en

  ```en
  Given array of strings words, return the smallest string that contains each string in words as a substring
  If there are multiple valid strings of the smallest length, return any of them
  Assume that no string in words is a substring of another string in words
  ```

* tc

  ```tc
  Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
  Output: "gctaagttcatgcatc"
  ```

## Solution

* py

  ```py
  def shortestSuperstring(self, words: List[str]) -> str:
    overlaps = [[0 for _ in range(len(words))] for _ in range(len(words))]
    for i, cur in enumerate(words):
      for j, nxt in enumerate(words):
        for k in range(1, len(cur)):
          if nxt.startswith(cur[k:]):
            overlaps[i][j] = len(cur) - k
            break

    @lru_cache(None)
    def dfs(i, mask):
      if mask == (1 << len(words)) - 1:
        return words[i]
      ans = '#' * 320
      for j in range(len(words)):
        if mask & (1 << j) == 0:
          string = dfs(j, mask | (1 << j))
          ans = min(ans, words[i] + string[overlaps[i][j]:], key = len)
      return ans

    return min([dfs(i, 1<<i) for i in range(len(words))], key=len)
  ```
