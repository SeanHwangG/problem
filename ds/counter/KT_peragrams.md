# [KT_peragrams](https://open.kattis.com/problems/peragrams)

* en

  ```en
  Peragrams is Palindrome when suffle it's character
  Given string, how many character should I remove to make Peragrams
  ```

* tc

  ```tc
  Input: abc
  Output: 0
  ```

## Solution

* py

  ```py
  from collections import Counter
  cnt = Counter()
  for ch in input():
    cnt[ch] += 1
  ret = 0
  for count in cnt:
    if cnt[count] % 2 == 1:
      ret += 1
  print(max(0, ret - 1))
  ```
