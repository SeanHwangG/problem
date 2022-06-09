# [KT_moscowdream](https://open.kattis.com/problems/moscowdream)

* en

  ```en

  ```

* kr

  ```kr
  첫줄에 a, b, c, d가 주어진다
  이는 각각 easy, medium, hard, total문제 개수 이다
  easy, medium, hard를 모두 포함하고, 총 문제 수가 total인 문제집을 만들 수 있으면 YES 아니면 NO를 출력하라
  ```

* tc

  ```tc
  Input: 0 3 3 5
  Output: NO
  ```

## Solution

* py

  ```py
  a, b, c, d = map(int, input().split())
  print("NO" if a == 0 or b == 0 or c == 0 or a + b + c < d or d < 3 else "YES)
  ```
