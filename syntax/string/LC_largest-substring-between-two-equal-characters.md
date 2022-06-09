# [LC_largest-substring-between-two-equal-characters](https://leetcode.com/problems/largest-substring-between-two-equal-characters)

* en

  ```en
  Given string s, return length of longest substring between 2 equal characters, excluding two characters
  If there is no such substring return -1.

  A substring is a contiguous sequence of characters within a string
  ```

* tc

  ```tc
  Input: s = "aa"
  Output: 0

  Input: s = "abca"  # bc
  Output: 2

  Input: s = "cbzxy"
  Output: -1
  ```

## Solution

* cpp

  ```cpp
  int maxLengthBetweenEqualCharacters(string s, unordered_map<char, int> m = {}, vector<int> cand = {}) {
    for_each(s.begin(), s.end(), [i = -1, &m](auto c) mutable { m[c] = ++i; });
    transform(s.begin(), s.end(), back_inserter(cand), [i = -1, &m](auto c) mutable { return m[c] - ++i - 1; });
    return *max_element(cand.begin(), cand.end());
  }
  ```

* py

  ```py
  def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    return max(s.rfind(ch) - s.find(ch) - 1 for ch in set(s))
  ```
