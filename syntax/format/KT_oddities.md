# [KT_oddities](https://open.kattis.com/problems/oddities)



```txt
Input: 2
1
2

Output:
1 is even
2 is odd
```

## Solution

* py

  ```py
  for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
      print(f"{n} is even")
    else:
      print(f"{n} is odd")
  ```
