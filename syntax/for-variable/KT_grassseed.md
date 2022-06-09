# [KT_grassseed](https://open.kattis.com/problems/grassseed)

* en

  ```en

  ```

* kr

  ```kr
  C 1m2 에 소모되는 씨앗의 가격
  L 라인 의 수
  w1 l1 밭의 넓이 높이
  wL lL
  이 때 총 씨앗의 가격을 구하라
  ```

* tc

  ```tc
  Input:
  0.75
  2
  2 3.333
  3.41 4.567

  Output: 16.6796025
  ```

## Solution

* py

  ```py
  c = float(input())
  l = int(input())
  ret = 0
  for _ in range(l):
    w, l = map(float, input().split())
    ret += w * l * c
  print(ret)
  ```
