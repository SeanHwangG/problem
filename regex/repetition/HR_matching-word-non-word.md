# [HR_matching-word-non-word](https://www.hackerrank.com/challenges/matching-word-non-word)

* en

  ```en
  You have a test string S. Your task is to match the pattern xxxXxxxxxxxxxxXxxx
  Here x denotes any word character and X denotes any non-word character
  ```

* tc

  ```tc
  Matches
  www.hk.com
  www.he.com
  www.123jhg-kup.com
  www.a-a.com
  www.aaaaaaa-aaaaaaaaaaaaaaaaaaaaaaaaaaa.com

  Non-Matches
  www.a.com
  www.bb-bbbb-bb.com
  ```

## Solution

* py

  ```py
  import re

  print(str(bool(re.search(r"\w{3}\W\w{10}\W\w{3}", input()))).lower())
  ```
