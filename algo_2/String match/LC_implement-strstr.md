# [LC_implement-strstr](https://leetcode.com/problems/implement-strstr)

* en

  ```en
  Return index of first occurrence of needle in haystack, or -1 if needle is not part of haystack
  ```

* tc

  ```tc
  Input: haystack = "hello", needle = "ll"
  Output: 2
  ```

## Solution

* cpp

  ```cpp
  class Solution {
  public:
    int strStr(string haystack, string needle) {
      int m = haystack.size(), n = needle.size();
      if (!n)
        return 0;
      vector<int> lps = kmpProcess(needle);
      for (int i = 0, j = 0; i < m;) {
        if (haystack[i] == needle[j])
          i++, j++;
        if (j == n)
          return i - j;
        if (i < m && haystack[i] != needle[j])
          j ? j = lps[j - 1] : i++;
      }
      return -1;
    }
  private:
    vector<int> kmpProcess(string needle) {
      int n = needle.size();
      vector<int> lps(n, 0);
      for (int i = 1, len = 0; i < n;) {
        if (needle[i] == needle[len]) lps[i++] = ++len;
        else if (len)                 len = lps[len - 1];
        else                          lps[i++] = 0;
      }
      return lps;
    }
  };
  ```

* py

  ```py
  def strStr(self, haystack: str, needle: str) -> int:
    concat = needle + '#' + haystack
    b, suffix = 0, [0]
    for i in range(1, len(concat)):
      while b > 0 and concat[i] != concat[b]:
        b = suffix[b - 1]
      if concat[b] == concat[i]:
        b += 1
      else:
        b = 0
      suffix.append(b)

    # 01000120 : suffix
    # ll#hello : concat
    n = len(needle)
    if n == 0:
      return n
    for i in range(n + 1, len(suffix)):
      if suffix[i] == n:
        return i - 2 * n
    return -1
  ```
