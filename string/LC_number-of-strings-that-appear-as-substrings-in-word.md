# [LC_number-of-strings-that-appear-as-substrings-in-word](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word)

Given array of strings patterns and string word, return # strings in patterns that exist as substring in word

```txt
Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3

Input: patterns = ["a","b","c"], word = "aaaaabbbbb"
Output: 2
```

## Solution

```cpp
int numOfStrings(vector<string>& ps, string word) {
  return count_if(begin(ps), end(ps), [&](const auto &p) { return word.find(p) != string::npos; });
}
```

```py
def numOfStrings(self, patterns: List[str], word: str) -> int:
  return sum(x in word for x in patterns)
```
