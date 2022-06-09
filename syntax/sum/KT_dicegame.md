# [KT_dicegame](https://open.kattis.com/problems/dicegame)

* en

  ```en

  ```

* kr

  ```kr
  두줄에 거쳐 총 8개의 수가 주어진다
  이 때 위 줄의 합이 크면 Emma 아랫줄의 합이 크면 Gunnar, 같을 시에는 Tie를 출력하라
  ```

* tc

  ```tc
  Input:
  3
  5 17
  *****************
  .............**$*
  *B*A*P*C**X*Y*.X.
  *y*x*a*p**$*$**$*
  *****************
  cz
  5 11
  *.*********
  *...*...*x*
  *X*.*.*.*.*
  *$*...*...*
  ***********
  0
  7 7
  *ABCDE*
  X.....F
  W.$$$.G
  V.$$$.H
  U.$$$.J
  T.....K
  *SQPML*
  irony

  Output:
  3
  1
  0
  ```

## Solution

* py

  ```py
  a = sum(map(int, input().split()))
  b = sum(map(int, input().split()))
  if a < b:
    print('Emma')
  elif b < a:
    print('Gunnar')
  else:
    print('Tie')
  ```
