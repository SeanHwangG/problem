# [KT_exam](https://open.kattis.com/problems/exam)

```en
First line number of correct from friend, and answer sheets from mine and my friend are given
Print maximum number of questions that I could have gotten right
```

```kr
첫째 줄에 친구가 맞은 개수, 두번째 세번째 줄에 나와 친구의 답지가 주어진다.
이때 내가 맞을수 있는 최대의 개수를 구하라
```

```txt
Input: 3
FTFFF
TFTTT

Output: 2
```

## Solution

* py

  ```py
  correct = int(input())
  my = input()
  fr = input()
  total = len(my)
  same = 0
  for m, f in zip(my, fr):
    if m == f:
      same += 1

  if same > correct:
    print(correct + (total - same))
  else:
    print(same + (total - correct))
  ```
