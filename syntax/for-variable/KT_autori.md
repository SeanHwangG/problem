# [KT_autori](https://open.kattis.com/problems/autori)

* en

  ```en

  ```

* kr

  ```kr
  Knuth-Morris-Pratt (KMP)
  Mirko-Slavko (MS)
  위와 같이 첫 글자와 - 다음에 나오는 단어를 축약시킬 수 있다. 왼쪽과 같은 인풋이 주어졌을 때 오른쪽과 같이 출력하라
  ```

* tc

  ```tc
  Input: Knuth-Morris-Pratt
  Output: KMP
  ```

## Solution

* py

  ```py
  st = input()
  for i, ch in enumerate(st):
    if i == 0 or st[i - 1] == '-':
      print(st[i], end='')
  ```
