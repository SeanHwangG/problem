# [KT_everywhere](https://open.kattis.com/problems/everywhere)



```txt
Input: 2
7
saskatoon
toronto
winnipeg
toronto
vancouver
saskatoon
toronto
3
edmonton
edmonton
edmonton

Output: 4
1
```

## Solution

* py

  ```py
  n_test = int(input())
  for _ in range(n_test):
    N = int(input())
    se = set()
    for _ in range(N):
      se.add(input())
    print(len(se))
  ```
