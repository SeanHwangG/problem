# [KT_everywhere](https://open.kattis.com/problems/everywhere)

* en

  ```en

  ```

* kr

  ```kr
  첫 줄에 테스트 케이스 수
  각 테스트 케이스는 N 과 N개의 줄에 도시이름이 주어진다. 이 때 다른 도시 개수를 출력하라
  ```

* tc

  ```tc
  Input: 2
  7
  saskatoon
  toronto
  winnipeg
  toronto
  vancouver
  saskatoon
  toronto
  3
  edmonton
  edmonton
  edmonton

  Output: 4
  1
  ```

## Solution

* py

  ```py
  n_test = int(input())
  for _ in range(n_test):
    N = int(input())
    se = set()
    for _ in range(N):
      se.add(input())
    print(len(se))
  ```
