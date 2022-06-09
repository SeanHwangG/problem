# [LC_check-if-one-string-swap-can-make-strings-equal](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal)

* en

  ```en
  Given two strings s1 and s2 of equal length
  String swap is an operation where you choose two indices in a string and swap the characters at these indices
  is it possible to make both strings equal by performing at most one string swap on exactly one of the strings
  ```

* tc

  ```tc
  Input: s1 = "bank", s2 = "kanb"
  Output: true
  ```

## Solution

* py

  ```py
  def areAlmostEqual(self, s1: str, s2: str) -> bool:
    diff = [[x, y] for x, y in zip(s1, s2) if x != y]
    return not diff or len(diff) == 2 and diff[0][::-1] == diff[1]
  ```
