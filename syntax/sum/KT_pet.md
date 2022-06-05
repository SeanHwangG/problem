# [KT_pet](https://open.kattis.com/problems/pet)

```en
When each participant is given an evaluation score, find the winner and his score
```

```kr
5명의 선수가 4명에게 점수를 받는다. 이 때 우승자와 그 점수를 구하라
```

```txt
Input:
5 4 4 5
5 4 4 4
5 5 4 4
5 5 5 4
4 4 4 5

Output: 4 19
```

## Solution

* py

  ```py
  num = mx = 0
  for i in range(5):
    temp = sum(map(int, input().split()))
    if mx < temp:
      mx = temp
      num = i + 1

  print(num, mx)
  ```
