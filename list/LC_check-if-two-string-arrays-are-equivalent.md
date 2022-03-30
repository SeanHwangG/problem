```cpp
bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
  return ranges::equal(word1 | views::join, word2 | views::join);
}
```
