# [HR_positive-lookahead](https://www.hackerrank.com/challenges/positive-lookahead)

* en

  ```en
  Write a regex that can match all occurrences of o followed immediately by oo in S
  ```

* tc

  ```tc
  Input: gooooo!
  Output: Number of matches : 3
  ```

## Solution

* py

  ```py
  import re

  Test_String = input()

  pattern = r"o(?=oo)"
  match = re.findall(pattern, Test_String)

  print("Number of matches :", len(match))
  ```
