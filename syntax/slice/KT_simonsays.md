# [KT_simonsays](https://open.kattis.com/problems/simonsays)

* en

  ```en

  ```

* kr

  ```kr
  첫줄에 N이 주어진다
  다음 N줄에 문자가 주어지는데, Simon says로 시작 할 시에, 이후에 나오는 행동을 출력하라
  ```

* tc

  ```tc
  Input:
  3
  Simon says raise your right hand.
  Lower your right hand.
  Simon says raise your left hand.

  Output:
   raise your right hand.
   raise your left hand.
  ```

## Solution

* py

  ```py
  N = int(input())
  for _ in range(N):
    s = input()
    if s[:10] == "Simon says":
      print(s[10:])
  ```
