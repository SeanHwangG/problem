# [HR_backreferences-to-failed-groups](https://www.hackerrank.com/challenges/backreferences-to-failed-groups)

* en

  ```en
  Consists of 8 digits
  \- separator such that string S gets divided in 4 parts, with each part having exactly two digits
  ```

* tc

  ```tc
  Input1: 12345678
  Output1: true

  Input2: 1-234-56-78
  Output2: false
  ```

## Solution

* py

  ```py
  import re
  pattern = r"^((\d{8})|(\d{2}-\d{2}-\d{2}-\d{2}))$"
  print(str(bool(re.search(pattern, input()))).lower())
  ```
