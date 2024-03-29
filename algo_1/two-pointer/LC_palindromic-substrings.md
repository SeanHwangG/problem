# [LC_palindromic-substrings](https://leetcode.com/problems/palindromic-substrings)

* en

  ```en
  Given a string s, return the number of palindromic substrings in it
  A substring is a contiguous sequence of characters within the string
  ```

* tc

  ```tc
  Input: s = "aaa"
  Output: 6
  ```

## Solution

* cpp

  ```cpp
  int countSubstrings(string s) {
    int res = 0, n = s.length();
    for(int i = 0; i < n; i++){
      //substring s[i-j, ..., i+j]
      for(int j = 0; i-j >= 0 && i+j < n && s[i-j] == s[i+j]; j++) res++;
      //substring s[i-1-j, ..., i+j]
      for(int j = 0; i-1-j >= 0 && i+j < n && s[i-1-j] == s[i+j]; j++) res++;
    }
    return res;
  }
  ```

* py

  ```py
  def countSubstrings(self, S):
    def manachers(S): # represents the maximum half-length of a palindrome at some center
      A = '@#' + '#'.join(S) + '#$'
      Z = [0] * len(A)
      center = right = 0
      for i in range(1, len(A) - 1):
        if i < right:
          Z[i] = min(right - i, Z[2 * center - i])
        while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
          Z[i] += 1
        if i + Z[i] > right:
          center, right = i, i + Z[i]
      return Z
    return sum((v + 1) // 2 for v in manachers(S))
  ```
