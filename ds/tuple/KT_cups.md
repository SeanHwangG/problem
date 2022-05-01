# [KT_cups](https://open.kattis.com/problems/cups)



```txt
Input:
3
red 10
10 blue
green 7

Output:
blue
green
red
```

## Solution

* py

  ```py
  n_line = int(input())
  li = []
  for _ in range(n_line):
    a, b = input().split()
    if a.isdigit():
      li.append((int(a), b))
    else:
      li.append((int(b) * 2, a))
  for _, color in sorted(li):
    print(color)
  ```
