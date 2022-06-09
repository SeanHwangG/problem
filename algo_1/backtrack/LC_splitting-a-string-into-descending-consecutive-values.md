# [LC_splitting-a-string-into-descending-consecutive-values](https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values)

* en

  ```en
  Check if we can split s into two or more non-empty substrings
  ST numerical values of substrings are in descending and diff between numerical values of adjacent substrings are 1
  ```

* tc

  ```tc
  Input: s = "050043"
  Output: true
  ```

## Solution

* cpp

  ```cpp
  bool splitString(string &s, int i = 0, long prev = 0) {
    long num = 0;
    for (int j = i; num < 1e+10 && j < s.size() - (i == 0 ? 1 : 0); ++j) {
      num = num * 10 + (s[j] - '0');
      if ((i == 0 || prev - 1 == num) && splitString(s, j + 1, num))
        return true;
    }
    return i == s.size();
  }
  ```

* py

  ```py
  def splitString(self, s: str, num=None) -> bool:
    if num is None:
      return any(self.splitString(s[i:], int(s[:i]) - 1) for i in range(1, len(s)))
    else:
      return len(s) == 0 or any(self.splitString(s[i:], num - 1) for i in range(1, len(s) + 1) if int(s[:i]) == num)
  ```
