# [KT_kemija08](https://open.kattis.com/problems/kemija08)

* en

  ```en

  ```

* kr

  ```kr
  루카는 화학 수업 시간에 지루해서 문단에 있는 모음(a,e,i,o,u) 을 모음p모음 으로 바꾸었다
  이 바뀐 문장을 원래대로 돌려라
  ```

* tc

  ```tc
  Input: zepelepenapa papapripikapa
  Output: zelena paprika
  ```

## Solution

* py

  ```py
  st = input()
  skip = 0
  for ch in st:
    if skip > 0:
      skip -=1
    elif ch in 'aeiou':
      skip = 2
      print(ch, end='')
    else:
      print(ch, end='')
  ```
