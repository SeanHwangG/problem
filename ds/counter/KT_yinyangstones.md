# [KT_yinyangstones](https://open.kattis.com/problems/yinyangstones)

* en

  ```en

  ```

* kr

  ```kr
  W와 B의 개수가 같으면 1 아니면 0을 출력하라
  ```

* tc

  ```tc
  Input: WWBWBB
  Output: 1
  ```

## Solution

* py

  ```py
  from collections import Counter
  cnt = Counter(input())
  print(1 if cnt['W'] == cnt['B'] else 0)
  ```
