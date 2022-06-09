# [LC_longest-palindrome](https://leetcode.com/problems/longest-palindrome)

* en

  ```en
  Given a string s which consists of lowercase or uppercase letters
  Return length of longest palindrome that can be built with those letters
  ```

* tc

  ```tc
  Input: s = "abccccdd"
  Output: 7
  ```

## Solution

* cpp

  ```cpp
  int longestPalindrome(string s) {
    int odds = 0;
    for (char c = 'A'; c <= 'z'; c++)
      odds += count(s.begin(), s.end(), c) & 1;
    return s.size() - odds + (odds > 0);
  }
  ```
