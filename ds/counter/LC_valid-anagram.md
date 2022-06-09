# [LC_valid-anagram](https://leetcode.com/problems/valid-anagram)

* en

  ```en
  Given two strings s and t, return true if t is an anagram of s, and false otherwise
  ```

* tc

  ```tc
  Input: s = "anagram", t = "nagaram"
  Output: true
  ```

## Solution

* cpp

  ```cpp
  bool isAnagram(string s, string t) {
    return unordered_multiset<char>(begin(s), end(s)) == unordered_multiset<char>(begin(t), end(t));
  }
  ```
