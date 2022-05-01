# [KT_parking](https://open.kattis.com/problems/parking)



```txt
Input:
5 3 1
1 6
3 5
2 8

Output: 33
```

## Solution

* py

  ```py
  n_test = int(input())
  for i in range(n_test):
    N = int(input())
    li = list(map(int, input().split()))
    print((max(li) - min(li)) * 2)
  ```
