# [LC_check-if-two-string-arrays-are-equivalent](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent)

Given two string arrays word1 and word2, return if two arrays represent same string
A string is represented by an array if the array elements concatenated in order forms the string


```txt
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true  # Both represent "abc"

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
```

## Solution

* cpp

```cpp
bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
  return ranges::equal(word1 | views::join, word2 | views::join);
}
```
