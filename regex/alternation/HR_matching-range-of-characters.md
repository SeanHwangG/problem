# [HR_matching-range-of-characters](https://www.hackerrank.com/challenges/matching-range-of-characters)

* en

  ```en
  first character must be a lowercase English alphabetic character
  second character must be a positive digit. Note that we consider zero to be neither positive nor negative
  third character must not be a lowercase English alphabetic character
  fourth character must not be an uppercase English alphabetic character
  fifth character must be an uppercase English alphabetic character
  ```

* tc

  ```tc
  Input: h4CkR
  Output: true
  ```

## Solution

* py

  ```py
  import re
  pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'
  print(str(bool(re.search(pattern, input()))).lower())
  ```
