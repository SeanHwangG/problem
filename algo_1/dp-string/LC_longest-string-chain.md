# [LC_longest-string-chain](https://leetcode.com/problems/longest-string-chain)

* en

  ```en
  wordA is predecessor of wordB iff 1 letter is inserted in wordA is to make it equal to wordB
  Return length of longest possible word chain with words chosen from the given list of words
  ```

* tc

  ```tc
  Input: words = ["a","b","ba","bca","bda","bdca"]
  Output: 4  # One of the longest word chains is ["a","ba","bda","bdca"].

  Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
  Output: 5  # All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

  Input: words = ["abcd","dbqca"]
  Output: 1  # The trivial word chain ["abcd"] is one of the longest word chains.
  ```

## Solution

* py

  ```py
  def longestStrChain(self, words: List[str]) -> int:
    dp = {}
    for w in sorted(words, key=len):
      dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
    return max(dp.values())
  ```
