# [KT_oddmanout](https://open.kattis.com/problems/oddmanout)

```en

```

```kr
n_test개의 줄에 N과 N개의 정수가 주어진다
이때 짝이 없는 정수를 출력하라
```

```txt
Input:
3
3
1 2147483647 2147483647
5
3 4 7 4 3
5
2 10 2 10 5

Output:
Case #1: 1
Case #2: 7
Case #3: 5
```

## Solution

* py

  ```py
  for test in range(1, int(input()) + 1):
    N = int(input())
    ret = 0
    for x in map(int, input().split()):
      ret ^= x
    print(f"Case #{test}: {ret}")
  ```
