# [KT_sevenwonders](https://open.kattis.com/problems/sevenwonders)

* en

  ```en

  ```

* kr

  ```kr
  문자열이 주어진다
  이 때 T, C, G 중 가장 적게 나온 개수 * 7 + T 개수^2 + C 개수^2 + G 개수^2 의 합을 구하라
  ```

* tc

  ```tc
  Input: TCGTTC
  Output: 21
  ```

## Solution

* py

  ```py
  from collections import Counter
  st = input()
  co = Counter(st)
  ret = min(co['T'], co['C'], co['G']) * 7
  ret += co['T'] ** 2
  ret += co['C'] ** 2
  ret += co['G'] ** 2

  print(ret)
  ```
