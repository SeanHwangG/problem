# [LC_detect-capital](https://leetcode.com/problems/detect-capital)

```en
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google"

```

```txt
Input: word = "USA"
Output: true

Input: word = "FlaG"
Output: false
```

## Solution

* cpp

  ```cpp
  bool detectCapitalUse(string word) {
    return all_of(word.begin(), word.end(), ::isupper) or all_of(next(word.begin()), word.end(), ::islower);
  }
  ```
