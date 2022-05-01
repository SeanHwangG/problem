# [KT_grassseed](https://open.kattis.com/problems/grassseed)



```txt
Input:
0.75
2
2 3.333
3.41 4.567

Output: 16.6796025
```

## Solution

* py

  ```py
  c = float(input())
  l = int(input())
  ret = 0
  for _ in range(l):
    w, l = map(float, input().split())
    ret += w * l * c
  print(ret)
  ```
