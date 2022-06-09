# [LC_valid-palindrome](https://leetcode.com/problems/valid-palindrome)

* en

  ```en
  Check if string is palindrome
  ```

* tc

  ```tc
  Input: s = "A man, a plan, a canal: Panama"
  Output: true
  ```

## Solution

* cpp

  ```cpp
  bool isPalindrome(string s) {
    int i = 0, j = s.size() - 1;
    while (i < j){
      while (!isalpha(s[i]) && !isdigit(s[i]))  i++;
      while (!isalpha(s[j]) && !isdigit(s[j]))  j--;
      if (i < j && tolower(s[i++]) != tolower(s[j--])) return false;
    }
    return true;
  }
  ```
