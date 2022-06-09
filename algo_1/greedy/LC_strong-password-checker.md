# [LC_strong-password-checker](https://leetcode.com/problems/strong-password-checker)

* en

  ```en
  It has at least 6 characters and at most 20 characters
  It contains at least one lowercase letter, at least one uppercase letter, and at least one digit
  It does not contain three repeating characters in a row
    (ex: "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met)
  Minimum nubmer of steps to make password strong
    Insert one character to password,
    Delete one character from password, or
    Replace one character of password with another character
  ```

* tc

  ```tc
  Input: password = "aA1"
  Output: 3
  ```

## Solution

* py

  ```py
  def strongPasswordChecker(self, s):
    missing_type = 3
    if any('a' <= c <= 'z' for c in s): missing_type -= 1
    if any('A' <= c <= 'Z' for c in s): missing_type -= 1
    if any(c.isdigit() for c in s): missing_type -= 1

    change = 0
    one = two = 0
    i = 2
    while i < len(s):
      if s[i] == s[i-1] == s[i-2]:
        length = 2
        while i < len(s) and s[i] == s[i-1]:
          length += 1
          i += 1

        change += length // 3
        if length % 3 == 0: one += 1
        elif length % 3 == 1: two += 1
      else:
        i += 1

    if len(s) < 6:
      return max(missing_type, 6 - len(s))
    elif len(s) <= 20:
      return max(missing_type, change)
    else:
      delete = len(s) - 20

      change -= min(delete, one)
      change -= min(max(delete - one, 0), two * 2) // 2
      change -= max(delete - one - 2 * two, 0) // 3

      return delete + max(missing_type, change)
  ```
