# [KT_basketballoneonone](https://open.kattis.com/problems/basketballoneonone)

* en

  ```en
  A + point 혹은 B + point와 같은 형식으로 점수를 출력 할 때 더 많은 점수를 얻는 사람을 출력하라
  ```

* tc

  ```tc
  Input: A2B1A2B2A1A2A2A2
  Output: A
  ```

## Solution

* py

  ```py
  s = input()
  A = B = 0
  for i in range(1, len(s), 2):
    if s[i - 1] == 'A':
      A += int(s[i])
    else:
      B += int(s[i])
  if A > B:
    print('A')
  else:
    print('B')
  ```
