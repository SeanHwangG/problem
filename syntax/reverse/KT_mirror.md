# [KT_mirror](https://open.kattis.com/problems/mirror)

```en
Print mirrored string
```

```kr
거울에 비친 글자를 출력하라
```

```txt
Input:
2
2 2
.*
..
4 4
***.
**..
....
....

Output:
Test 1
..
*.
Test 2
....
....
..**
.***
```

## Solution

* py

  ```py
  n_test = int(input())
  for test in range(1, n_test + 1):
    R, C = map(int, input().split())
    G = [input() for _ in range(R)]
    print(f"Test {test}")
    for st in reversed(G):
      print("".join(reversed(st)))
  ```
