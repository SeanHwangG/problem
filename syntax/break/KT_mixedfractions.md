# [KT_mixedfractions](https://open.kattis.com/problems/mixedfractions)

In each line a, b are given and input ends with 0 0
Print a / b in mixed number form

```txt
Input: 27 12  # a, b
2460000 98400
3 4000
0 0
Output:
2 3 / 12
25 0 / 98400
0 3 / 4000
```

## Solution

* py

  ```py
  while True:
    dem, num = map(int, input().split())
    if dem == num == 0:
      break
    print(dem // num, dem % num, '/', num)
  ```
