# [KT_alphabetspam](https://open.kattis.com/problems/alphabetspam)

* en

  ```en

  ```

* kr

  ```kr
  첫줄에 문장이 주어진다
  이 때 문장에서 _의 비율, 소문자의 비율, 대문자의 비율, 나머지 부호의 비율을 각각 출력하라
  ```

* tc

  ```tc
  Input: Welcome_NWERC_participants!
  Output:
  0.0740740740740741
  0.666666666666667
  0.222222222222222
  0.0370370370370370
  ```

## Solution

* py

  ```py
  st = input()
  white, lower, upper, symbol = 0, 0, 0, 0
  for ch in st:
    if ch == '_':
      white += 1
    elif ch.islower():
      lower += 1
    elif ch.isupper():
      upper += 1
    else:
      symbol += 1

  total = white + lower + upper + symbol
  print(white / total)
  print(lower / total)
  print(upper / total)
  print(symbol / total)
  ```
