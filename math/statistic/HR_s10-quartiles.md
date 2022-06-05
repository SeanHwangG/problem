# [HR_s10-quartiles](https://www.hackerrank.com/challenges/s10-quartiles)

```en
Print quartile Q1, Q2, Q3
```

```txt
Input:
9
3 7 8 5 12 14 21 13 18

Output:
6
12
16
```

## Solution

* py

  ```py
  from statistics import median
  input()
  arr= list(sorted(map(int, input().split())))
  t = int(len(arr) / 2)
  if len(arr) % 2==0:
    L = arr[:t]
    U = arr[t:]
  else:
    L = arr[:t]
    U = arr[t+1:]

  print(int(median(L)))
  print(int(median(arr)))
  print(int(median(U)))
  ```
