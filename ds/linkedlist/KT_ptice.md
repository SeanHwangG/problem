# [KT_ptice](https://open.kattis.com/problems/ptice)

* en

  ```en
  Repeat ABC, BABC, CCAABB
  Find whose sequence contains the most correct answers
  ```

* tc

  ```tc
  Input:
  5
  BAACC

  Output:
  3
  Bruno
  ```

## Solution

* py

  ```py
  length = int(input())
  li = list(input())
  a = ['A', 'B', 'C']
  b = ['B', 'A', 'B', 'C']
  g = ['C', 'C', 'A', 'A', 'B', 'B']
  scores = [0, 0 , 0]
  for i in range(length):
    if li[i] == a[i % 3]:
      scores[0] += 1
    if li[i] == b[i % 4]:
      scores[1] += 1
    if li[i] == g[i % 6]:
      scores[2] += 1

  print(max(scores))
  if max(scores) == scores[0]:
    print('Adrian')
  if max(scores) == scores[1]:
    print('Bruno')
  if max(scores) == scores[2]:
    print('Goran')
  ```
